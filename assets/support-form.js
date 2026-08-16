/* Vectored support form.
   Upgrades the support pages' ticket form to post JSON at the same endpoint
   as the feedback page, replacing the old fire-and-forget Google Forms iframe
   (which could not report a rejected submission, carried no product field, and
   sent no notification).

   Include after feedback-config.js — and after feedback-templates.js on any
   page whose form has no data-tool, so the tool <select> can be populated:

     <form id="feedback-form" data-vc-support data-tool="apistudio"> … </form>
     <script src="<path>/assets/feedback-config.js"></script>
     <script src="<path>/assets/support-form.js"></script>

   data-tool fixes the product for a per-product support page. Omit it and the
   form renders a tool picker instead (used by the site-level support page).
   Fields are read by name: type, subject, message, email, name, company. */
(function () {
  'use strict';

  var form = document.querySelector('form[data-vc-support]');
  if (!form) return;

  var CFG = window.VECTORED_FEEDBACK_CONFIG || {};
  var REG = window.VectoredFeedback;
  var successBox = document.getElementById('form-success');
  var errorBox = document.getElementById('form-error');
  var tool = form.getAttribute('data-tool') || '';
  var submitting = false;

  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
    });
  }

  // Site-level page: offer the same tool list the feedback form uses.
  var picker = form.querySelector('[name="tool"]');
  if (!tool && picker && REG) {
    var html = '<option value="" disabled selected>Choose a tool…</option>';
    REG.list().forEach(function (t) {
      var suffix = t.badge && t.badge !== 'LIVE' ? ' (' + t.badge.toLowerCase() + ')' : '';
      html += '<option value="' + t.id + '">' + esc(t.name) + (t.platform ? ' — ' + esc(t.platform) : '') + suffix + '</option>';
    });
    picker.innerHTML = html;
    // ?tool= on the URL preselects it, matching the feedback page's behaviour.
    var q = new URLSearchParams(location.search).get('tool');
    var resolved = q && REG.resolve(q);
    if (resolved) picker.value = resolved.id;
  }

  function fieldValue(name) {
    var el = form.querySelector('[name="' + name + '"]');
    return el ? String(el.value || '').trim() : '';
  }

  function showError(msg, payload) {
    if (!errorBox) return;
    errorBox.innerHTML = esc(msg) + ' <button type="button" class="underline font-semibold cursor-pointer">Send it as an email instead</button> — nothing you typed is lost.';
    errorBox.classList.remove('hidden');
    errorBox.querySelector('button').addEventListener('click', function () { mailFallback(payload); });
  }

  function mailFallback(payload) {
    var lines = [];
    Object.keys(payload).forEach(function (k) {
      if (k === 'userAgent' || payload[k] === '' || payload[k] == null) return;
      lines.push(k + ': ' + payload[k]);
    });
    window.location.href =
      'mailto:' + (CFG.FALLBACK_EMAIL || 'support@vectored.dev') +
      '?subject=' + encodeURIComponent('[Support] ' + (payload.toolName || 'Vectored') + ' — ' + (payload.subject || '')) +
      '&body=' + encodeURIComponent(lines.join('\n'));
  }

  function succeed(id) {
    form.classList.add('hidden');
    if (errorBox) errorBox.classList.add('hidden');
    if (!successBox) return;
    successBox.classList.remove('hidden');
    var ref = successBox.querySelector('[data-ref]');
    if (ref && id) {
      ref.textContent = 'Reference ' + id;
      ref.classList.remove('hidden');
    }
    successBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }

  function setBusy(on) {
    submitting = on;
    var btn = form.querySelector('[type="submit"]');
    if (!btn) return;
    btn.disabled = on;
    btn.classList.toggle('opacity-60', on);
    btn.textContent = on ? 'Sending…' : 'Submit';
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (submitting) return;

    var chosen = tool || fieldValue('tool');
    var subject = fieldValue('subject');
    var message = fieldValue('message');
    var email = fieldValue('email');

    if (!chosen || !subject || !message) {
      showError('Fill in the tool, subject and description first.', {});
      return;
    }
    if (email && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
      showError('That email address does not look right.', {});
      return;
    }

    var tpl = REG ? REG.template(chosen) : null;
    var payload = {
      tool: chosen,
      toolName: tpl ? tpl.name : chosen,
      templateId: tpl ? tpl.id : chosen,
      type: fieldValue('type'),
      subject: subject,
      message: message,
      email: email,
      name: fieldValue('name'),
      company: fieldValue('company'),
      // Support tickets carry no rating; the field stays null in the table.
      contactBack: email ? 'yes' : 'no',
      source: 'support-page',
      pageUrl: location.href,
      referrer: document.referrer || '',
      userAgent: navigator.userAgent,
      submittedAt: new Date().toISOString(),
    };

    if (!CFG.ENDPOINT) { mailFallback(payload); return; }

    setBusy(true);
    fetch(CFG.ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload),
    })
      .then(function (r) {
        return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, body: j }; });
      })
      .then(function (res) {
        if (!res.ok) throw new Error(res.body && res.body.error ? res.body.error : 'Request failed');
        succeed(res.body && res.body.id);
      })
      .catch(function (err) {
        setBusy(false);
        showError('We could not send that (' + (err.message || 'network error') + ').', payload);
      });
  });

  // "Submit another" resets back to a clean form.
  var again = successBox && successBox.querySelector('[data-reset]');
  if (again) again.addEventListener('click', function () {
    successBox.classList.add('hidden');
    form.classList.remove('hidden');
    form.reset();
    setBusy(false);
  });
})();
