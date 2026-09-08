# Use Watch Video directly in ChatGPT

## Architecture

ChatGPT calls this repository's small HTTPS service. The service authenticates ChatGPT,
passes a public YouTube URL or temporary uploaded-video download to Gemini, and returns
the resulting Markdown. `GEMINI_API_KEY` never enters ChatGPT, source control, or the API
response.

Analysis runs as a background job so long videos do not have to finish inside one Action
request. Keep one service instance and persistent storage mounted at `/data` (or replace
SQLite with a managed job store before scaling to multiple instances).

## 1. Deploy the service

Deploy `skills/watch-video/Dockerfile` to an HTTPS container host such as Google Cloud
Run, Render, Railway, or Fly.io. Configure these as secrets/environment variables:

- `GEMINI_API_KEY`: the private Gemini key.
- `ACTION_API_KEY`: a different, long random value used only between ChatGPT and this
  service.
- `PUBLIC_BASE_URL`: the service's public HTTPS origin when the host does not supply
  `RENDER_EXTERNAL_URL` automatically. Render users do not need to set this.

For the initial personal Ikhaya setup, configure one running instance and a persistent
volume mounted at `/data`. Do not make the Action unauthenticated. Confirm that
`https://YOUR-DOMAIN/health` returns `{"status":"ok"}`.

## 2. Create or edit the GPT

This requires a ChatGPT account or managed workspace that currently exposes GPT editing
and Custom Actions. If **Create/Edit GPT** or **Actions** is absent, ask the workspace
owner to enable it; the service can still be deployed, but it cannot be attached to that
ChatGPT account through this route.

In ChatGPT's GPT editor, add a new Action and import:

`https://YOUR-DOMAIN/openapi.json`

The imported schema must show `create_analysis` and `get_analysis` as available actions.
If ChatGPT reports that `servers` has no valid URL, confirm that the host supplies
`RENDER_EXTERNAL_URL`, or set `PUBLIC_BASE_URL` to the service's HTTPS origin and
redeploy.

Choose API-key authentication, select **Custom header**, use `X-Action-Key` as the header
name, and paste the same `ACTION_API_KEY` value stored by the host. Do not use the Gemini
key here.

Add these GPT instructions:

```text
When the user asks to analyse a public YouTube URL or an attached video, call
create_analysis. For an attachment, send its generated openaiFileIdRefs value; do not
invent or expose a download link. Poll get_analysis using the returned job_id until the
status is complete or failed. Return the completed analysis substantially intact, then
answer the user's question. Separate direct observations from interpretations. For
Ikhaya work, extract reusable Etsy, Pinterest and social creative principles without
copying the source creator. Never claim social proof, metrics or facts the video does not
support.
```

Test first with a short public YouTube video, then with a small MP4 attachment. A hook
analysis can use `clip: "0:00-0:05"` and `fps: 10`. Use the default sampling for a full
long-form tutorial.

YouTube requests that specify a clip or custom FPS use Gemini's `videoMetadata`
interface. Whole-video requests and uploaded files continue through the Interactions
API.

## One-time user steps

1. Deploy the container and attach persistent `/data` storage.
2. Add `GEMINI_API_KEY` and a newly generated `ACTION_API_KEY` in the host's secret
   settings.
3. Create/edit a GPT, import `/openapi.json`, and configure the custom auth header.
4. Paste the GPT instructions above and run the two smoke tests.

The existing local command remains available and continues to read `GEMINI_API_KEY`
from the local environment.

## Privacy and operations

- Video content is sent to Google Gemini for analysis. Tell users before analysing
  private or sensitive uploads.
- Temporary uploaded videos are deleted locally as soon as the Gemini request finishes.
- Job results remain in the SQLite database. Treat the persistent volume as private and
  periodically remove old jobs according to your retention needs.
- Rotate either key immediately if it is exposed. Never add `.env`, the database, or
  copied videos to Git.
- A GPT can use either Apps or Actions, not both at once. Action availability and domain
  permissions depend on the ChatGPT account/workspace.
