# Christmas Gift Organiser — Real Product Proof Source Map

**Prepared:** 16 September 2026  
**Status:** QA-PASSED PRODUCTION INPUT  
**Purpose:** Remove ambiguity about the source of real product proof for first-wave Pinterest production without rebuilding the product.

## Authoritative product source

Google Sheet: `Ikhaya Christmas Gift Organiser Master v2`  
Spreadsheet ID: `1PcWpHYDs2Ig3xK4C9cqxoze0BB3U5i3NRO6qyaGIpFU`

Verified 16 September 2026:

- locale: `en_GB`
- timezone: `Europe/London`
- six tabs, in order:
  1. Dashboard
  2. People & Ideas
  3. Gift Tracker
  4. Budget
  5. Don't Forget
  6. Start Here

This master is the source of truth for product screenshots used in Christmas traffic creative. Do not use the older Drive copies unless the owner explicitly changes the source of truth.

## Pin proof mapping

### Pin 1 — product demonstration
Use:
- Dashboard as dominant proof
- Gift Tracker as supporting crop
- People & Ideas as supporting crop

### Pin 3 — budget intent
Use:
- Budget as dominant proof
- Dashboard budget/spend summary as supporting proof

### Pin 2 — mental-load problem
Use:
- approved calm lifestyle imagery
- Dashboard as recognisable product proof occupying at least one-third of the meaningful visual area

### Pin 4 — gift-idea capture
Use:
- People & Ideas as dominant proof
- crop the working idea/interests/sizes/links area rather than showing an unreadably small full sheet

## Dashboard visual verification

The master Dashboard was exported and visually inspected on 16 September 2026. It contains recognisable Christmas-specific product proof including:

- `Christmas Gift Organiser` heading
- total budget / spent so far / remaining summary
- gifts bought and days-to-Christmas indicators
- `YOUR CHRISTMAS AT A GLANCE` section
- buying / wrapping / posting / people-with-ideas status
- shopping and wrapping progress
- Ikhaya Designs GB branding and calm cream/forest-green/cranberry styling

This confirms it is commercially suitable as the Pin 1 hero and should not be replaced by a fake spreadsheet mockup.

## Production dependency discovered

The master Sheet can be exported successfully from Google Drive. However, the current unattended connector path cannot egress the locally rendered screenshot directly into Canva: the Canva asset upload rejected the generated local screenshot as an unavailable connector file reference.

This is a tooling/connector boundary, not a missing product asset. Do not respond by recreating the spreadsheet, generating fake UI, or changing the product.

At the next interactive Canva production opportunity, use the authoritative master Sheet above to capture/import the real Dashboard, Gift Tracker and People & Ideas proof, then implement Pin 1 using `first-wave-visual-production-board.md`.

## QA loop

### CREATE
Established the authoritative master and mapped its real tabs to each first-wave Pin.

### CRITIQUE
Risk: multiple Drive copies could cause stale screenshots; a blocked Canva upload could tempt production to use generated spreadsheet imagery; source proof could be too vague for a future operator.

### FIX
Pinned the exact master ID, verified UK locale/timezone and six-tab structure, visually inspected the Dashboard export, prohibited fallback to fake UI, and recorded the precise connector boundary.

### RE-CHECK
- authoritative source unambiguous: PASS
- product truth aligned with existing distribution board: PASS
- real-product-proof requirement preserved: PASS
- no unnecessary product rebuild: PASS
- future operator handover clear: PASS

## PASS

Real-product-proof sourcing is production-ready. The remaining Pin 1 implementation dependency is transferring the real screenshots into Canva through an interactive/compatible asset path and committing the customer-facing design behind the applicable owner approval gate.
