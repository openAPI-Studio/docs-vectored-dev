/* Vectored feedback endpoint config.
   Set ENDPOINT to the Lambda Function URL printed by `npx ampx sandbox` /
   Amplify deploy logs (amplify_outputs.json -> custom.feedbackFunctionUrl).

   While ENDPOINT is empty the form still validates and renders, but submitting
   falls back to a prefilled mail draft to FALLBACK_EMAIL so no feedback is lost. */
window.VECTORED_FEEDBACK_CONFIG = {
  ENDPOINT: '',
  FALLBACK_EMAIL: 'feedback@vectored.dev',
  DOCS_URL: 'https://docs.vectored.dev',
  REDIRECT_SECONDS: 10,
};
