/* Vectored feedback endpoint config.

   ENDPOINT points at the vectored.dev Amplify rewrite rather than the raw
   Lambda Function URL, matching how the landing page calls /api/contact — the
   path then survives function redeploys. The rewrite target is
   custom.feedbackFunctionUrl from the Amplify deploy output.

   This is a cross-origin call (docs.vectored.dev -> vectored.dev); the function
   answers the preflight itself and sets Access-Control-Allow-Origin.

   If ENDPOINT is empty or the request fails, the form falls back to a prefilled
   mail draft to FALLBACK_EMAIL so no feedback is lost. */
window.VECTORED_FEEDBACK_CONFIG = {
  ENDPOINT: 'https://vectored.dev/api/feedback',
  FALLBACK_EMAIL: 'feedback@vectored.dev',
  DOCS_URL: 'https://docs.vectored.dev',
  REDIRECT_SECONDS: 10,
};
