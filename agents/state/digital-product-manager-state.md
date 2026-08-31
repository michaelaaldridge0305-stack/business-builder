# Digital Product Manager State

**Updated:** 31 August 2026
**Status:** WORDPRESS PAYMENT PLAN SETUP - OWNER ACTION REQUIRED

## Current priority

Complete the native WordPress.com £19 one-time payment plan and digital-delivery configuration for Numbers to Management Narrative, then integrate the payment button into the existing draft and complete pre-publication QA.

## Owner decisions carried forward

- On 25 August 2026, Michaela decided not to undertake further independent human testing before progressing this product. Do not return to that gate unless materially new evidence changes the risk. Do not claim independent validation.
- On 27 August 2026, Michaela approved the completed customer package and the £19 launch price.
- On 28 August 2026, Michaela explicitly confirmed creation of the draft WordPress product page.
- On 31 August 2026, Michaela confirmed Stripe is connected to Ikhaya Automations.
- On 31 August 2026, Michaela confirmed permission to upload the approved customer files and update the existing draft page. Do not publish without a separate final publication approval.

## Work completed

1. Customer pack completed and QA-passed.
2. Editable DOCX and PDF package completed.
3. Final customer files were regenerated in the active runtime from the approved customer pack and visually inspected page by page. A numbering defect found during QA was corrected and the seven-page package was re-rendered and rechecked.
4. Listing, FAQ and launch copy completed at the approved £19 price.
5. Publication-ready website copy and metadata completed.
6. Draft WordPress page exists: page ID 74, slug `numbers-to-management-narrative`.
7. Stripe connection is now confirmed by the owner.
8. WordPress site capabilities were rechecked. The site exposes the `jetpack/payment-buttons` block required for the native WordPress.com payment route.
9. Current WordPress.com support documentation was reviewed. The recommended digital-product workflow remains: upload files, create a one-time payment plan in Jetpack > Monetize, put the download links in the welcome message, then assign the plan to a Payment Buttons block.
10. Exact payment-plan settings, welcome message, button wording and owner handoff are documented at `products/ai-quality-system/numbers-to-management-narrative-payment-setup.md`.

## WordPress draft

- Page ID: 74
- Status: draft
- Title: Numbers to Management Narrative
- Slug: numbers-to-management-narrative
- Approved price: £19
- Stripe: connected
- Purchase state: not yet functional
- Publication state: unpublished

## Current technical/platform gate

The connected WordPress MCP surface exposes content, media and page operations and confirms the Payment Buttons block is registered, but it does not expose a WordPress.com Monetize operation for creating the payment plan itself. The £19 one-time payment plan therefore has to be created through the WordPress admin interface.

The final DOCX and PDF are available in the active runtime and have passed visual QA. The WordPress media connector accepts raw base64 rather than a local binary file reference, so the reliable route at this gate is to upload the two files through WordPress Media while creating the Monetize plan.

## Owner action required now

Use the exact handoff in `products/ai-quality-system/numbers-to-management-narrative-payment-setup.md`:

1. Upload the approved DOCX and PDF to WordPress Media.
2. Copy their media URLs.
3. Go to Jetpack > Monetize > Payment Settings > Add a new payment plan.
4. Create `Numbers to Management Narrative` as a **one-time sale**, **GBP**, **£19**, customer-pick-price **off**, paid-newsletter-tier **off**.
5. Put both download URLs into the prepared welcome message and save the plan.
6. Do not publish the product page.

## Automatic action after owner completes this gate

Resume the existing draft, replace the placeholder purchase text with the approved `Get the toolkit - £19` payment-button configuration where the connector permits it, run page/content/claim QA, confirm the purchase path is internally coherent, update repository state and stop only at the final irreversible publication approval or another genuine platform limitation.
