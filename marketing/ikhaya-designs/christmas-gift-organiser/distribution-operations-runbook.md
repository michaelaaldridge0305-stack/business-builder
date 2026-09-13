# Christmas Gift Organiser — Distribution Operations Runbook

**Business:** Ikhaya Designs GB  
**Product:** Christmas Gift Organiser Google Sheets  
**Created:** 13 September 2026  
**Status:** QA-PASSED INTERNAL OPERATIONS ASSET

## Purpose

Turn the approved Christmas Gift Organiser distribution strategy into a repeatable publishing workflow that reduces owner effort and prevents the recent generated-text failures from reaching Pinterest or Instagram.

This runbook does not rebuild the product. It operationalises the existing first-wave distribution package.

## Current publication stack

Preferred scheduling route: **Metricool**, once the Ikhaya Pinterest account is connected to the Metricool brand.

Current Metricool brand timezone: `Europe/London`.

Current connection check on 13 September 2026: the Metricool brand exists but `networksData` is empty, so Pinterest is not yet available for API scheduling through Metricool.

Until Pinterest is connected, publishing remains a manual Pinterest action and should not be represented as automated.

## First-wave priority order

Use the existing approved sequence:

1. Pin 1 — product demonstration
2. Pin 3 — budget intent
3. Pin 2 — problem led
4. Pin 4 — gift ideas
5. Reel / short-form video — calm outcome scenario

No paid advertising at this stage.

## Mandatory preflight before any customer-facing asset is scheduled

### 1. Product truth check

Confirm every claim matches the live product:

- Dashboard
- People & Ideas
- Gift Tracker
- Budget
- Don't Forget
- Start Here
- Google Sheets delivery model
- access PDF containing the Google Sheets link

Do not mention features not present in the live product.

### 2. Visual text regression check

Recent generated assets failed because spaces were corrupted into stray `n` characters and because `DISTILL` was misspelled. Therefore every visual must be inspected character by character before PASS.

Check:

- every headline;
- every subheading;
- every CTA;
- every tab name;
- every logo/brand line;
- every visible word inside product mockups that was AI-generated or recreated;
- all punctuation and apostrophes;
- spacing between every word;
- no stray `n` characters replacing spaces;
- no dropped letters;
- no doubled words;
- no malformed characters;
- British spelling where applicable;
- no em dashes in customer-facing Ikhaya copy.

If any generated screenshot contains unreadable or invented micro-text, reject it rather than relying on the viewer not noticing.

### 3. Mobile thumbnail check

At Pinterest-feed size, confirm:

- headline is readable without zooming;
- product remains recognisable as a Google Sheets organiser;
- CTA is readable;
- decorative imagery does not overpower the product;
- no text is clipped;
- no element looks accidentally misaligned;
- foreground/background contrast is sufficient.

### 4. Destination consistency check

Before scheduling, confirm:

- Pin promise matches the Etsy listing;
- link goes directly to the Christmas Gift Organiser listing;
- Pin title and description use the correct angle for the visual;
- no outdated price is embedded in the creative;
- `Google Sheets` is clear where buyer expectations could otherwise be ambiguous.

## Metricool scheduling protocol

Once Pinterest is connected:

1. Read Metricool brand settings and use its returned timezone.
2. Check scheduled posts for the target date to avoid duplicate posting.
3. Use the approved Pin title and description from `distribution-conversion-pack.md`.
4. Use the exact Pinterest board selected for the Christmas product. Preferred board name from strategy: **Christmas Planning & Gift Organisation**.
5. Set the Etsy listing as the Pin link.
6. Use automatic publication only after the visual has passed the mandatory preflight.
7. Re-read the scheduled post returned by Metricool and verify title, link, board, date/time and media before treating scheduling as complete.

## Manual Pinterest fallback

If Metricool is not connected:

- do not create a duplicate schedule elsewhere;
- prepare the exact title, description, link, board and publication time;
- surface one manual owner action only;
- once the owner confirms the manual action is complete, record it and move on.

## Post-publication measurement

Record signals in this order of commercial value:

1. Etsy orders attributed or plausibly downstream from the campaign
2. Etsy listing visits
3. Etsy favourites
4. Pinterest outbound clicks
5. Pinterest outbound CTR
6. Saves
7. Impressions

Do not optimise for saves or impressions alone.

### First review window

Do not declare a creative winner immediately after publication. Allow enough data for the first wave to produce comparable signals, then compare:

- angle;
- outbound clicks;
- outbound CTR;
- Etsy downstream behaviour;
- whether product-led or lifestyle-led creative produces stronger commercial intent.

Reuse winning **angles**, not identical artwork.

## QA loop

### CREATE

Converted the existing Christmas distribution strategy into an operational publishing and QA runbook.

### CRITIQUE

**Commercial reviewer:** risk of turning the workflow into process overhead rather than distribution.  
**Brand reviewer:** risk of repeating the recent typo/text-generation failures.  
**Operator:** risk of assuming Metricool can publish when Pinterest is not connected.  
**Buyer:** risk of traffic creative promising more than the live Etsy listing proves.

### FIX

- Kept the runbook limited to publication-critical checks.
- Added character-by-character visual text inspection.
- Added explicit rejection criteria for unreadable AI-generated micro-text.
- Added live Metricool connection status and no-false-automation rule.
- Preserved the existing first-wave order instead of inventing new strategy.
- Added destination consistency and post-publication commercial measurement rules.

### RE-CHECK

- Product rebuild avoided: PASS
- Distribution bottleneck addressed: PASS
- Text-corruption regression covered: PASS
- Platform dependency made explicit: PASS
- Commercial measurement tied to Etsy outcomes: PASS
- Owner workload minimised: PASS

## PASS

This internal operations asset is ready for use. The only current external dependency is Pinterest being connected to the Metricool brand before scheduling can be executed through Metricool.