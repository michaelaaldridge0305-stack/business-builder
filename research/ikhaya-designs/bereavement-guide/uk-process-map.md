# UK Bereavement Administration Process Map

**Research date:** 9 September 2026
**Stage:** PROCESS RESEARCH
**Purpose:** Factual baseline for product validation, not customer-facing legal advice.

## Core journey

The authoritative England and Wales journey is: register the death, notify government and non-government organisations, arrange the funeral, check bereavement benefits and effects on the survivor's tax/benefits/pension, value the estate and assess Inheritance Tax, apply for probate where required, settle debts/taxes and administer/distribute the estate.

This is not one universal UK process. Scotland and Northern Ireland have material differences in registration, terminology and estate procedure, so a product should not present a single UK-wide checklist without jurisdiction routing.

## England and Wales

### Death certification and registration

GOV.UK states that a doctor confirms the death before contacting the medical examiner. The medical examiner checks the cause of death and the medical examiner's office confirms when registration can proceed. Registration is normally required within 5 days of that confirmation. After registration, the registrar issues the certificate for burial or cremation.

Where a death is reported to a coroner, registration and documentation differ. If an inquest is held, an interim death certificate can be used for probate and Tell Us Once while awaiting the final certificate.

### Tell Us Once and private organisations

Tell Us Once can notify most government organisations for someone who was living in England, Scotland or Wales. It must normally be used within 28 days of receiving the reference number. It does not remove the need to deal with many private organisations. GOV.UK specifically identifies banks, mortgage providers, insurers, utilities/contract providers, landlords/housing associations and many personal/workplace pension schemes as separate contacts.

### Estate and probate

Before applying for probate, the personal representative needs to check whether probate is required, estimate the estate's value, determine whether full estate details must be reported to HMRC and start paying Inheritance Tax if due. For estates requiring full reporting, form IHT400 is due within 12 months of death and before probate. Inheritance Tax is generally due by the end of the sixth month after death to avoid interest.

Probate applications differ depending on whether there is a will. Estate administration then includes settling debts and taxes, dealing with assets and distributing the estate according to the will or intestacy rules.

## Scotland

A death in Scotland should be registered within 8 days where possible. mygov.scot states that the registrar needs the Medical Certificate of Cause of Death. Scotland uses different estate/probate terminology and procedure from England and Wales. Tell Us Once is available for people living in Scotland and includes Social Security Scotland alongside UK government bodies.

A future product must route Scottish users to Scottish authoritative sources rather than merely changing the registration deadline in an England/Wales workflow.

## Northern Ireland

Northern Ireland has a distinct process. nidirect states that deaths should normally be registered within 5 days, except where referred to the coroner. Tell Us Once is not available to people who were living in Northern Ireland. Instead, the Northern Ireland Bereavement Service can report a death for Social Security benefits, State Pension and Pension Credit and check eligibility for relevant bereavement/funeral payments.

Northern Ireland also has its own probate process. nidirect describes Grants of Probate where there is a will and Grants of Letters of Administration where there is not. The probate application and estate-summary requirements are jurisdiction-specific.

## Death abroad

For a death abroad, GOV.UK says the death must be registered with local authorities in the country of death. UK registration is optional. Tell Us Once can still be available if the person normally lived in England, Scotland or Wales and was abroad temporarily. Bringing the body home creates additional documentation and coroner requirements in some circumstances.

## Information and documents as an organisational problem

The process repeatedly requires the bereaved person or personal representative to collect and reuse identifying details, certificates, account information, asset/debt information, contact records and reference numbers. Northern Ireland's official guidance explicitly provides a list of documents and information to gather after a death. GOV.UK estate-valuation guidance similarly requires identifying assets, debts and organisations, then requesting date-of-death values.

This supports testing an information-control system rather than a long explanatory ebook.

## Product-design implications from process research

1. A useful system should distinguish **urgent / first days**, **next few weeks**, and **estate administration / later** rather than present one undifferentiated master list.
2. It should distinguish **government notifications** from **private organisations still requiring contact**.
3. It should provide a reusable information/document record so users do not repeatedly reconstruct the same details.
4. It should provide a contact/action log with organisation, date, method, person/reference, documents sent, outcome, follow-up date and status.
5. Probate and tax content should function as decision-point signposting to authoritative sources, not as personalised advice.
6. Jurisdiction must be explicit. A single static whole-UK procedural checklist would carry avoidable accuracy risk.
7. Exceptional routes such as coroner/inquest and death abroad should be signposted as branches, not allowed to overwhelm the core workflow.

## Primary sources

- GOV.UK, What to do after someone dies / registration: https://www.gov.uk/after-a-death
- GOV.UK, Tell Us Once: https://www.gov.uk/after-a-death/organisations-you-need-to-contact-and-tell-us-once
- GOV.UK, coroner route: https://www.gov.uk/after-a-death/when-a-death-is-reported-to-a-coroner
- GOV.UK, death abroad: https://www.gov.uk/after-a-death/death-abroad
- GOV.UK, valuing an estate: https://www.gov.uk/valuing-estate-of-someone-who-died
- GOV.UK, applying for probate: https://www.gov.uk/applying-for-probate/before-you-apply
- GOV.UK, settling debts and taxes: https://www.gov.uk/probate-estate/settling-debts-and-taxes
- mygov.scot, Register a death, updated 30 July 2026: https://www.mygov.scot/register-death
- mygov.scot, Tell Us Once, updated 6 August 2026: https://www.mygov.scot/tell-us-once
- nidirect, Registering a death: https://www.nidirect.gov.uk/articles/registering-death-district-registrar
- nidirect, Bereavement Service: https://www.nidirect.gov.uk/articles/bereavement-service-reporting-death
- nidirect, Probate: https://www.nidirect.gov.uk/articles/probate
- nidirect, Documents and information needed: https://www.nidirect.gov.uk/articles/documents-and-information-needed-when-someone-dies
