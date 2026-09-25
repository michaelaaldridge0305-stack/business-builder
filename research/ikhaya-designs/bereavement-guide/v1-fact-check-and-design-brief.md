# V1 Fact Check & Design Brief

**Date:** 10 September 2026
**Status:** QA PASSED AT CONTENT LEVEL — ENGLAND-ONLY SCOPE AND EXPANDED SUPPORT SECTION VERIFIED; READY FOR VISUAL PRODUCTION

## Authoritative fact check

The v1 content build was checked against current GOV.UK guidance immediately after owner build approval.

### Confirmed

- GOV.UK's current step-by-step route includes registering the death, Tell Us Once/government notification, funeral arrangements, bereavement support/benefits, valuing the estate, checking whether probate is required, and dealing with the estate.
- GOV.UK explicitly states that organisations outside government, including employers, private pension providers, banks and utility companies, may still need to be told. This supports the product's private-organisation tracking layer.
- Tell Us Once currently applies where the person who died was living in England, Scotland or Wales (subject to the service conditions), and does not apply where the person was living in Northern Ireland or permanently abroad.
- A registrar can explain Tell Us Once and provide the reference/process. The product correctly avoids presenting Tell Us Once as universal.
- Estate valuation requires identifying assets and debts and is needed before a probate application where probate is required. The product correctly uses discovery and information-request tracking rather than attempting to calculate tax.
- GOV.UK states probate may be needed rather than universally required. The product uses conditional wording.
- GOV.UK provides separate routes where a death is reported to a coroner or occurs abroad. The product correctly signposts rather than trying to reproduce those processes.

### Content revision from fact check

The content architecture is sound. During visual production, use the GOV.UK wording hierarchy as a reference but do not imply the product's Now/Soon/Later groupings are statutory deadlines or a mandatory sequence. Tell Us Once should remain phrased as conditional and should not be represented as notifying private organisations.

## Official production links

- What to do when someone dies: https://www.gov.uk/when-someone-dies
- Tell Us Once: https://www.gov.uk/after-a-death/organisations-you-need-to-contact-and-tell-us-once
- Applying for probate: https://www.gov.uk/applying-for-probate
- Valuing an estate: https://www.gov.uk/valuing-estate-of-someone-who-died
- Death abroad: https://www.gov.uk/after-a-death/death-abroad

## England-only reconciliation and specialist support QA — 20 September 2026

### Practical administration: PASS

Fresh checks against current GOV.UK guidance confirmed:

- The England product correctly begins with registration and branches to the separate coroner, death-abroad and stillbirth routes rather than pretending one process fits every death.
- GOV.UK's live journey continues through government notification, funeral arrangements, possible bereavement benefits, the survivor's own benefits/tax/pension position, support, estate valuation, probate where required and estate administration.
- Tell Us Once is correctly described as conditional rather than universal. It is available where the person lived in England, Scotland or Wales, including some temporary deaths abroad, and must be used within 28 days of receiving the unique reference number.
- Tell Us Once does not close private financial and household accounts. Banks, mortgage providers, insurers, utilities, landlords or housing associations and many pension schemes may still require direct contact.
- Probate is correctly described as something that may be required, not an automatic requirement.
- Estate valuation and Inheritance Tax are signposted to current GOV.UK guidance rather than calculated inside the organiser.
- No fixed probate fee, tax threshold or other volatile amount is embedded.
- Now / Soon / Later remains an organisational aid, not a claim about statutory deadlines.

### Emotional-support section: PASS

The new support half was reviewed for tone, safeguarding and scope:

- It explicitly rejects a fixed timetable or compulsory stages of grief.
- Grounding and reflection are optional, low-intensity prompts and are not presented as treatment.
- It does not diagnose, promise recovery or imply that a printable replaces professional care.
- Child and baby loss, suicide bereavement, Armed Forces-related bereavement, former carers, and children and young people are signposted without claiming that these experiences are interchangeable.
- The remembrance prompts use original Ikhaya wording. No unverified literary, film or spiritual quotation has been included.
- Urgent-risk wording now matches NHS guidance: NHS 111 and the mental-health option for urgent help; 999 or A&E where life is at risk or someone cannot keep themselves or another person safe.

### Support-route verification: PASS

Checked against the organisations' current official pages:

- Samaritans: 116 123, free day or night.
- Sands: 0808 164 3332 for people affected by pregnancy loss or the death of a baby.
- Survivors of Bereavement by Suicide: 0300 111 5065; peer-led support for adults impacted by suicide loss.
- SSAFA: the unreliable bereavement-specific link was replaced with the current central Get Help route; Forcesline 0800 260 6780.
- Carers UK: current Life After Caring guidance retained.
- Cruse: current organisation and suicide-bereavement routes retained. The site rejected automated page retrieval during this QA pass, so precise service hours or telephone claims have deliberately not been embedded.

### Corrections made

1. Narrowed the product itself to England, while retaining factual references to Wales only where a UK-wide service's eligibility genuinely includes Wales.
2. Replaced the stale SSAFA bereavement URL.
3. Added verified urgent-help wording and telephone numbers.
4. Changed the support-list wording so peer listening, counselling, clinical care and emergency response are not conflated.
5. Removed the old readiness claim until this fresh check was complete; content readiness is now restored.

## Visual production brief

### Objective

Turn the approved content into a calm, highly usable working organiser that looks distinctly Ikhaya Designs GB and makes the administrative control system visibly more valuable than a free checklist.

### Format

- Primary: A4 portrait PDF suitable for home printing and tablet annotation.
- Do not force wide tables into unreadably small portrait layouts.
- Contact tracking should use either two linked portrait pages or a carefully designed landscape insert if needed.
- Aim for approximately 30-36 functional pages after repeated working sheets.
- Maintain generous writing space.

### Brand direction

- Ikhaya Designs GB only.
- Calm green and warm-neutral palette.
- Restrained eucalyptus/botanical accents, never decorative clutter.
- No pink.
- Clean, crisp typography and strong hierarchy.
- Calm and capable, not sombre, sentimental, funereal or clinical.
- Use the actual Ikhaya Designs GB logo on the final branded page in production when the approved asset is available.

### Page hierarchy

Each working page should make three things immediately obvious:
1. What this page is for.
2. What the user needs to record or do.
3. What is still outstanding.

Use short helper text. Avoid long paragraphs. Where procedural guidance is referenced, visually distinguish **Check official guidance** from an action field.

### High-value hero pages

Give greatest design attention to:
- Your Next Steps: Now / Soon / Later
- First Actions Dashboard
- Contact & Follow-up Log
- Important Documents tracker
- Accounts / Assets discovery
- Estate Information Request Tracker
- Outstanding Actions Review

These pages are the product's commercial differentiation and should dominate later Etsy/Pinterest previews.

### Accessibility / usability

- Body text must remain comfortably readable when printed at 100% A4.
- Strong contrast between text and background.
- Do not rely on colour alone for status meaning.
- Checkboxes and writing fields must be large enough to use by hand.
- Avoid dense grey text and excessive italics.
- Avoid large decorative areas that consume writing space.
- Repeated logs should have consistent columns and status vocabulary.

### Status vocabulary

Use consistently where applicable:
- Not started
- Waiting
- Follow up
- Done
- N/A where genuinely useful

### Production QA checklist

Before the designed product can reach owner approval:
- every content section from the authorised specification is represented;
- all official links work;
- England scope is prominent;
- disclaimers are legible but not alarmist;
- no legal/tax/probate outcome is presented as personalised advice;
- no passwords/PIN/security-answer fields exist;
- no volatile fees or thresholds have slipped into the product;
- tables have adequate handwriting/typing space;
- print legibility is checked;
- page numbering and version date are consistent;
- no overlapping or clipped elements;
- botanical graphics do not interfere with working areas;
- final product is self-reviewed from a bereaved buyer's perspective, not merely a design perspective.

## Gate

No further owner decision is required for the approved England-only conversion. That fresh specialist fact check is now complete. Visual production may proceed. Final publication still requires a last link/contact check, rendered-product QA and owner approval. Final product publication, pricing, and any material scope change remain escalation points.