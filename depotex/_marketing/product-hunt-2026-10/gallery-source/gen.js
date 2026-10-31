const { chromium } = require('playwright');
const fs = require('fs');
const SHIELD = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/></svg>';
const css = `
@font-face{font-family:DMS;src:url(dmserif.woff2)}
*{box-sizing:border-box;margin:0;padding:0}
body{width:1270px;height:760px;overflow:hidden;font-family:Inter,sans-serif;color:#0f172a;background:#f8fafc}
.wrap{display:flex;height:100%;}
.left{width:430px;padding:56px 44px 44px 56px;display:flex;flex-direction:column}
.brand{display:flex;align-items:center;gap:10px;font-family:DMS;font-size:22px}
.mark{width:34px;height:34px;border:1px solid #cbd5e1;border-radius:8px;background:#fff;display:flex;align-items:center;justify-content:center;color:#1e293b}
.mark svg{width:20px;height:20px}
.eyebrow{margin-top:64px;font-family:'JetBrains Mono';font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#64748b}
h1{font-family:DMS;font-weight:400;font-size:46px;line-height:1.08;margin-top:14px;letter-spacing:-.01em}
p{margin-top:20px;font-size:18px;line-height:1.5;color:#475569}
ul{margin-top:22px;list-style:none}
li{font-size:16px;color:#334155;padding:6px 0 6px 22px;position:relative;line-height:1.4}
li:before{content:'';position:absolute;left:2px;top:14px;width:7px;height:7px;border-radius:50%;background:#1e293b}
.right{flex:1;position:relative;overflow:hidden}
.shot{position:absolute;border-radius:14px;border:1px solid #e2e8f0;box-shadow:0 20px 60px rgba(15,23,42,.14),0 2px 8px rgba(15,23,42,.06);background:#fff;overflow:hidden}
.shot img{display:block;width:100%}
.code{position:absolute;left:260px;top:300px;width:520px;background:#0f172a;color:#e2e8f0;border-radius:14px;padding:22px 26px;font-family:'JetBrains Mono';font-size:15px;line-height:1.75;box-shadow:0 20px 60px rgba(15,23,42,.25)}.code .ct{color:#94a3b8;font-size:12px;letter-spacing:.14em;text-transform:uppercase;margin-bottom:8px}.code i{color:#94a3b8;font-style:normal}.dark{background:#0f172a;color:#f8fafc}
`;
const slide = (o) => `<html><head><style>${css}</style></head><body><div class="wrap">
<div class="left"><div class="brand"><div class="mark">${SHIELD}</div>Depotex</div>
<div class="eyebrow">${o.eyebrow}</div><h1>${o.title}</h1>${o.body?`<p>${o.body}</p>`:''}${o.list?`<ul>${o.list.map(x=>`<li>${x}</li>`).join('')}</ul>`:''}</div>
<div class="right">${o.shots.map(s=>`<div class="shot" style="left:${s.x}px;top:${s.y}px;width:${s.w}px${s.h?`;height:${s.h}px`:''}"><img src="${s.src}"></div>`).join('')}${o.extra||''}</div></div></body></html>`;

const slides = [
 {f:'01-dashboard', eyebrow:'Self-hosted artifact repository', title:'Every package your teams build and use, on a server you run.', body:'18 package formats behind one address. One server or a cluster, with the same features either way.', shots:[{src:'dashboard-overview.png',x:20,y:60,w:900}]},
 {f:'02-browse', eyebrow:'18 formats · hosted, proxy, group', title:'Keep your package managers. Change one URL.', list:['Maven, npm, PyPI, Docker &amp; OCI, Helm, Go, NuGet, Cargo','APT, YUM, Terraform, Hugging Face, Git LFS','Composer, RubyGems, Conda, Conan, Raw','Proxies cache public registries, so builds keep working offline'], shots:[{src:'browse-search.png',x:20,y:60,w:900}]},
 {f:'03-quarantine', eyebrow:'Supply-chain security', title:'Hold bad versions back, even through proxies.', list:['Quarantine new or suspect versions until someone releases them','“New npm versions wait 3 days” in one rule','Block list refuses a version everywhere','Integrity checks on every stored file'], shots:[{src:'quarantine.png',x:20,y:50,w:800}]},
 {f:'04-sbom', eyebrow:'SBOMs &amp; vulnerabilities', title:'See what every version is made of.', list:['Reads SPDX and CycloneDX stored with artifacts','Finds a component everywhere it is used','Checks against OSV vulnerability data','Export, share and score SBOM completeness'], shots:[{src:'sbom-version.png',x:20,y:90,w:900}]},
 {f:'05-ai-agents', eyebrow:'AI-ready (MCP)', title:'Let AI agents find artifacts, as you.', list:['MCP tools: search artifacts, read SBOMs and docs, get download links','OAuth sign-in per person: agents never do more than you can','Write tools off by default; quarantine and release only','Rate limits and prompt-injection labels built in'], shots:[{src:'mcp-crop.png',x:40,y:70,w:560}], extra:`<div class="code"><div class="ct">MCP tools</div>${['search_artifacts','get_artifact_metadata','get_sbom','get_vulnerabilities','search_components','search_docs','get_download_link','vibe_search · vibe_pull · vibe_diff','quarantine_version <i>(opt-in)</i>','release_from_quarantine <i>(opt-in)</i>'].map(x=>`<div>${x}</div>`).join('')}</div>`},
 {f:'06-vibe', eyebrow:'Vibe artifacts', title:'A home for what AI coding tools build.', list:['Push code, memory, known gaps and screenshots per check-in','Milestones, “last passing” and rollback','Every push scanned for secrets and hidden characters','Find projects by name, date or screenshot'], shots:[{src:'vibe-project.png',x:20,y:40,w:820}]},
 {f:'07-backups', eyebrow:'Operations', title:'Backups you have actually restored.', list:['Encrypted, verified backups to a separate target','Weekly test restores compare every table','Disaster recovery from the CLI or the setup wizard','System check, audit log, Prometheus metrics'], shots:[{src:'backups-list.png',x:20,y:120,w:820}]},
 {f:'08-platform', eyebrow:'Built for platform teams', title:'Rules before, automation after.', list:['Every major operation is an event','Policies block, warn or adjust, with a dry run first','Alerts, webhooks and email after the fact','SSO, LDAP, SCIM; PostgreSQL, Redis optional; S3, MinIO, Azure'], shots:[{src:'policies-editor.png',x:20,y:40,w:760}]},
];
(async()=>{
 const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1270,height:760},deviceScaleFactor:2});
 const out = process.argv[2];
 for (const s of slides){ fs.writeFileSync(s.f+'.html', slide(s)); await p.goto('file://'+process.cwd()+'/'+s.f+'.html'); await p.waitForTimeout(300); await p.screenshot({path:`${out}/${s.f}.png`}); }
 // thumbnail
 fs.writeFileSync('thumb.html',`<html><body style="margin:0;width:240px;height:240px;background:#1e293b;display:flex;align-items:center;justify-content:center;color:#fff"><div style="width:130px;height:130px">${SHIELD}</div></body></html>`);
 const t = await b.newPage({viewport:{width:240,height:240}}); await t.goto('file://'+process.cwd()+'/thumb.html'); await t.screenshot({path:`${out}/thumbnail-240.png`});
 await b.close();
})();
