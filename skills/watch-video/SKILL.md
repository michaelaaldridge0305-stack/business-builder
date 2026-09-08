---
name: watch-video
description: Analyze a public YouTube video or a local video file using Gemini's native video understanding. Use this when the user asks what happens in a video, why a video or hook works, how the visuals/editing/captions are structured, what marketing lessons can be extracted, or how to adapt the underlying structure for Ikhaya Designs or Ikhaya Automations without copying the creator.
---

# Watch Video

Use `watch_video.py` in this folder to inspect the actual video frames and audio rather than relying only on captions or a transcript.

## When to use

Use this skill for:
- YouTube videos and saved video files.
- Reels, TikToks and Shorts supplied as local files.
- Hook and editing analysis.
- Visual merchandising and product-presentation analysis.
- Etsy, Pinterest and Instagram creative research.
- Turning long tutorials into practical playbooks.
- Comparing several creator videos to identify repeatable patterns.

For Ikhaya work, pay particular attention to visual hierarchy, thumbnail/cover readability, product visibility, framing, crop safety, captions, pacing, proof, benefit communication and the gap between an attractive image and an image that actually sells the product.

## Inputs

Required:
- `source`: public YouTube URL or local video path.

Optional:
- `--clip START-END`: only inspect a specific range, e.g. `0:00-0:05`.
- `--fps N`: frame sampling rate.
- `--prompt "..."`: replace the standard report with a specific question.
- `--model MODEL`: override the Gemini model.

## Choose frame rate before running

- Short-form, fast-cut video: use about 6-10 fps.
- Hook analysis: use `--clip 0:00-0:05 --fps 10`.
- Long talking-head videos, tutorials, podcasts and screen recordings: use the default sampling rate.
- Do not use a high frame rate across a long video. Clip the range first.

## Run

From the repository root:

```bash
python skills/watch-video/watch_video.py "<source>" [flags]
```

The environment must contain `GEMINI_API_KEY`.

## Use from ChatGPT

The `service.py` wrapper exposes this skill as an authenticated Custom GPT Action. It
accepts either a public YouTube URL or one video attached to the ChatGPT message, starts
the Gemini analysis asynchronously, and lets ChatGPT poll for the completed Markdown.

Deployment and one-time ChatGPT setup are in [CHATGPT_SETUP.md](CHATGPT_SETUP.md).
The Gemini key belongs only in the hosting provider's secret settings. The separate
Action key belongs in both the host and ChatGPT's Action authentication settings; neither
secret belongs in this repository or in a conversation.

## Accuracy rules

- Describe only what the analysis actually supports.
- Never invent a creator, speaker, quote, statistic, product, brand or voiceover.
- Distinguish observation from interpretation.
- Preserve returned timestamps rather than estimating or tidying them.
- If no speech is present, say so.
- If a YouTube URL is inaccessible because it is private, restricted or otherwise unsupported, ask for the video file instead.
- Treat creator analysis as research: extract principles and reusable structure, not copied creative assets or wording.

## Default output

Return the report from the script substantially intact, then answer the user's specific question. For marketing analysis, conclude with concrete lessons that can be applied to Ikhaya while keeping the Ikhaya brand distinct.

## Ikhaya creative-analysis lens

When relevant, add these questions to the analysis:
1. What makes the first frame or thumbnail stop the scroll?
2. Is the product/result immediately obvious at mobile size?
3. What visual proof is shown rather than merely claimed?
4. How does the creator move from pain/problem to solution?
5. Which elements survive aggressive thumbnail cropping?
6. What creates perceived professionalism or trust?
7. What would be useful to adopt as a principle, and what should not be copied?
8. How could the principle improve an Etsy hero image, secondary listing image, Pinterest pin or Instagram post for Ikhaya?
