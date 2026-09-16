# Digital Product Manager State

**Updated:** 16 September 2026
**Status:** ACTIVE ACROSS BOTH IKHAYA BUSINESSES

## Primary execution source

The Product Manager operates through:

`operating-system/PRODUCT_MANAGER_CONTROL_CENTRE.md`

Read that control centre at the beginning of every Product Manager run. It contains the live commercial queue, GREEN / AMBER / RED authority model, definition of complete, execution loop, reporting format and autonomy test.

This state file preserves strategic constraints. If the control centre and this file differ on current task priority, use the newer explicit owner direction and then the control centre. Do not override the strategic business constraints below without explicit owner direction.

## Operating scope

Treat **Ikhaya Automations** and **Ikhaya Designs GB** as distinct businesses.

### Ikhaya Automations

Education and audience-building remain the primary model. The immediate paid-product push remains paused. Do not restart `Numbers to Management Narrative` or begin another Ikhaya Automations paid product unless Michaela explicitly reauthorises it. Research-led educational work remains authorised. External publication remains an owner approval gate where required.

### Ikhaya Designs GB

Ikhaya Designs GB creates practical digital tools that help people move **from chaos to calm**. It is not a planner shop. Etsy is the primary sales channel. Pinterest is primarily a qualified traffic/discovery channel to Etsy. Instagram is a supporting awareness channel.

## Current priority order

### Priority 1: Christmas Gift Organiser commercial completion

**Current status:** INTERNAL DISTRIBUTION PACKAGE, OPERATIONS RUNBOOK, REEL HANDOVER, FIRST-WAVE VISUAL PRODUCTION BOARD AND REAL-PRODUCT-PROOF SOURCE MAP COMPLETE. RENDERED PIN IMPLEMENTATION REMAINS ACTIVE. CANVA PERSISTENT EDITS/PUBLISHING REQUIRE THE APPLICABLE OWNER GATE; METRICOOL PINTEREST CONNECTION REMAINS THE EXTERNAL SCHEDULING DEPENDENCY.

The revamped Christmas Gift Organiser remains the first autonomy test. Product rebuilding is not the current bottleneck.

Completed internal assets:

- `marketing/ikhaya-designs/christmas-gift-organiser/distribution-conversion-pack.md`
- `marketing/ikhaya-designs/christmas-gift-organiser/distribution-operations-runbook.md`
- `marketing/ikhaya-designs/christmas-gift-organiser/reel-production-handover.md`
- `marketing/ikhaya-designs/christmas-gift-organiser/first-wave-visual-production-board.md`
- `marketing/ikhaya-designs/christmas-gift-organiser/real-product-proof-source-map.md`

Recommended first wave remains Pins 1, 3, 2, 4 plus the short-form Reel, organically first. No paid Pinterest advertising.

**Owner direction / QA incident:** Michaela deleted a previously produced Reel because it contained repeated text corruption where the letter `n` appeared instead of spaces. A later Notion Pin also required correction because `DISTILL` was misspelled. These defects are mandatory visual-QA regression checks for all generated customer-facing assets: inspect rendered text character by character for stray letters, corrupted spaces, spelling errors, malformed punctuation and AI artefacts before PASS.

Michaela explicitly authorised proceeding with visual production. Do not recreate or publish defective assets unchanged.

**14 September 2026 Reel direction:** Landscape footage cannot be centre-cropped into 9:16 when that removes the woman, because the relaxed person is the meaning of the scenario. Blurred-background conversion was rejected because it makes the meaningful footage too small. The approved route is a native 1080 x 1920 lifestyle still with subtle Canva movement, followed by a real-product dashboard proof scene and a short closing CTA. All customer-facing copy must be editable Canva text, not AI-generated text embedded in imagery. The full QA-passed assembly specification is stored in `reel-production-handover.md`.

**15 September 2026 Pin production direction:** The existing Canva `Untitled (Pinterest Pin)` was inspected. It remains a 3-page 1000 x 1500 design with generic `Stay Calm & Organized This Christmas` messaging and reusable image fills. It is not approved unchanged. A QA-passed production board now specifies exact layouts, product-proof requirements, copy, metadata and rendered-file acceptance criteria for Pins 1, 3, 2 and 4. Every first-wave Pin must use real product screenshots and must pass phone-thumbnail and character-level QA before publication.

**16 September 2026 source-of-truth verification:** Google Drive was searched and `Ikhaya Christmas Gift Organiser Master v2` (spreadsheet ID `1PcWpHYDs2Ig3xK4C9cqxoze0BB3U5i3NRO6qyaGIpFU`) was verified as the authoritative product source. It is `en_GB`, `Europe/London` and contains Dashboard, People & Ideas, Gift Tracker, Budget, Don't Forget and Start Here. The Dashboard was exported and visually inspected and is suitable real product proof for Pin 1. A durable source map is stored in `real-product-proof-source-map.md`. The unattended Canva connector cannot currently ingest the locally rendered screenshot because the connector rejects that generated file reference. Do not work around this by generating fake spreadsheet UI. Use the real master screenshots at the next compatible interactive Canva implementation opportunity.

The connected Canva workflow requires an approval gate before persistent design commits, so unattended runs may inspect and prepare but must not silently commit customer-facing Canva changes. The Reel additionally has a genuine manual Canva sequencing/timing dependency.

A live Metricool connection check on 13 September 2026 found the Ikhaya brand and `Europe/London` timezone, but `networksData` is empty. Pinterest is therefore not yet connected to the Metricool brand and API scheduling cannot be treated as available until that connection exists.

### Priority 2: optimise existing Etsy listings and Pinterest traffic

Continue systematic Etsy listing audits using the SmallBizSis-derived framework and the standard established with the Notion Guide. Prioritise listings with stronger demand signals where data is available.

The 13 Week Cash Flow Forecast has a QA-passed internal Pinterest distribution package at `marketing/ikhaya-designs/13-week-cash-flow-forecast/pinterest-distribution-pack.md`. External visual production/posting remains behind the applicable approval gate.

### Priority 3: England & Wales bereavement administration organiser

Research and commercial validation have completed and the narrowed England & Wales v1 build was explicitly approved by Michaela on 10 September 2026. Work is on `codex/bereavement-validation`. Do not let it displace time-sensitive Christmas distribution.

### Priority 4: continue Ikhaya Automations education work

Continue research-led education and audience building when higher-priority Designs work is not actionable.

## Ikhaya Designs GB operating principles

- Core promise: practical tools that help people move from chaos to calm.
- Do not position the business as a planner shop.
- Prefer clean, calm, practical, professional design.
- Avoid pink unless specifically requested.
- Use the correct Ikhaya Designs GB logo where appropriate.
- Green/neutral styling and restrained botanical/eucalyptus elements may be used where suitable.
- Customer-facing language should be human, useful and specific.
- Do not use em dashes in customer-facing copy.
- Product/listing images must be inspected for clipping, overlap, blank areas, unreadable text, poor hierarchy, incorrect logos and weak thumbnail performance.
- Generated visual text must be inspected character by character for corrupted spacing, stray letters, spelling errors and other AI text artefacts before PASS.
- Never assume a scheduler/integration is operational. Verify the network connection before describing publication as automated.

## Management by exception

Continue authorised internal work without repeatedly asking Michaela to continue. Escalate only for genuine owner decisions, permissions, publication approvals, spending, strategic forks, consequential external actions, missing owner-only facts, material risk, or a formal validation decision gate.

## Next autonomous action

At the next compatible owner-approved Canva implementation opportunity, produce Pin 1 from `first-wave-visual-production-board.md` using screenshots from the verified master Sheet identified in `real-product-proof-source-map.md`; run rendered-file QA before progressing to Pin 3, Pin 2 and Pin 4. Do not substitute generated spreadsheet UI if screenshot transfer is blocked. Once Pinterest is connected to Metricool, use the runbook to schedule only QA-passed assets and record outbound clicks/downstream Etsy signals. Do not rebuild the Christmas product or repeat failed landscape-video conversion approaches.