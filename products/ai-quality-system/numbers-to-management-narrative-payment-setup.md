# Numbers to Management Narrative - WordPress Payment and Delivery Setup

**Prepared:** 31 August 2026
**Status:** Stripe connected. Manual WordPress Monetize configuration required before checkout can be completed.
**Approved price:** £19 GBP, one-time sale

## Confirmed platform route

Use the existing Ikhaya Automations WordPress.com Premium site and its native Payment Buttons feature rather than introducing another paid platform.

WordPress.com support documentation reviewed on 31 August 2026 confirms the intended digital-product flow:

1. Connect Stripe.
2. Upload the digital files to the WordPress media library.
3. Go to Jetpack > Monetize > Payment Settings.
4. Create a new payment plan.
5. Set it as a one-time sale.
6. Set the price and currency.
7. Put the product download link(s) in the welcome message.
8. Save the payment plan.
9. Add a Payment Buttons block to the product page and assign the payment plan.

WordPress emails the welcome message to a successful buyer. Anyone with the direct media URL can access the file, so this is a lightweight delivery route rather than controlled ecommerce. That limitation is acceptable for the £19 launch product unless owner strategy changes.

## Exact payment plan settings

**Plan name:** Numbers to Management Narrative

**Renewal frequency:** One-time sale

**Currency:** GBP

**Amount:** £19

**Customer chooses own amount:** Off

**Paid newsletter tier:** Off

## Recommended welcome message

Thank you for purchasing Numbers to Management Narrative.

Your toolkit includes an editable Word document and a PDF reference copy.

Download the files here:

- Editable toolkit: [DOCX DOWNLOAD LINK]
- PDF reference copy: [PDF DOWNLOAD LINK]

Please save your own copies after downloading.

Use the toolkit only in line with your organisation's information-security, privacy and AI-use policies. AI output remains a drafting and challenge aid. Final professional judgement and sign-off remain with you.

## Product-page button

**Button label:** Get the toolkit - £19

Assign the `Numbers to Management Narrative` one-time payment plan to this button.

## Current technical limitation

The connected WordPress MCP surface exposes content/page/media operations and confirms that the `jetpack/payment-buttons` block is registered on the site, but it does not expose an operation for creating or editing WordPress.com Monetize payment plans. Payment-plan creation therefore has to be completed through the WordPress admin interface by the owner.

The connector's media upload action accepts raw base64 rather than a local file reference. The final customer files have been regenerated and visually QA-checked in the active runtime, but the automated connector surface cannot reliably bridge those local binary files into the WordPress Monetize setup without embedding their full binary payload into an action. Prefer the normal WordPress Media upload UI at this gate.

## Owner action required

In WordPress:

1. Upload `Numbers-to-Management-Narrative.docx` and `Numbers-to-Management-Narrative.pdf` to Media.
2. Copy both media URLs.
3. Go to Jetpack > Monetize > Payment Settings > Add a new payment plan.
4. Use the exact payment-plan settings above.
5. Paste the two media links into the welcome message and save the plan.

Do not publish the product page yet.

Once this payment plan exists, the Product Manager can resume page-level checkout integration and pre-publication QA through available WordPress operations, subject to any further platform confirmation gate.
