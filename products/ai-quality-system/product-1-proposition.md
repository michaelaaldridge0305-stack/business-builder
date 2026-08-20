# Ikhaya Product 1 — Proposition v0.1

**Status:** Product strategy, not build specification
**Date:** 20 August 2026

## Decision

Do not build a generic “AI Workday System” or a prompt pack. Narrow Product 1 towards UK finance and finance-adjacent professionals who already use, or want to use, general-purpose AI for work where accuracy and judgement matter.

Working positioning:

> **Use AI for work you actually have to get right.**

The product should teach a repeatable method for accelerating real finance/admin work while retaining human verification, traceability and decision ownership.

## Core customer

Initial customer hypothesis: UK finance and finance-adjacent professionals, especially finance managers, management accountants, analysts, bookkeepers and operations/admin professionals with recurring reporting or decision-support responsibilities.

They are not necessarily AI beginners. A particularly attractive customer is someone who has already tried ChatGPT/Claude/Copilot, seen useful results, but does not yet trust the output enough to make AI part of a repeatable work process.

## Job-to-be-done

“When I use AI on important work, help me get useful output faster without creating a second job checking everything or risking a confident but wrong result.”

## Distinctive framework

Every workflow follows:

**Input → Context → Process → Checks → Output → Human decision**

The differentiator is not the prompt. The defensible asset should be the **Checks** layer: task-specific verification procedures, evidence/traceability, failure modes, escalation points, and explicit human decision ownership.

A generic disclaimer saying “always check AI output” is not sufficient.

## Three proposed core jobs

### 1. Numbers → Management Narrative

**Job:** Turn an already-validated spreadsheet/reporting pack into a first-pass explanation of performance for a non-technical stakeholder.

**Why it belongs:** Recurring monthly use; close to the target customer’s real work; clear before/after output; high consequence of subtle error; existing free AI can generate prose but does not itself create a reliable verification discipline.

**Boundary:** AI should not be trusted to establish the underlying financial truth. The human validates source numbers/variance calculations first. AI assists with interpretation, structure, questions and narrative.

**Checks should include:** source-number traceability; separation of fact from inference; unsupported-causation detection; materiality; period/comparator consistency; missing-context flags; final human sign-off.

### 2. Challenge My Work Before My Manager Does

**Job:** Review a report, proposal, business case or recommendation and systematically challenge assumptions, evidence, gaps and likely stakeholder objections before submission.

**Why it belongs:** Claude’s research found this comparatively underserved; it uses AI as critic rather than generic writer; consequence and perceived value are high even if frequency is lower.

**Boundary:** AI critique is another perspective, not an authority. Domain judgement remains with the user.

**Checks should include:** distinguish factual defects from stylistic preferences; require critique to point to evidence; identify where AI lacks organisational context; classify issues by consequence; human accepts/rejects each challenge.

### 3. Messy Evidence → Checked Structured Output

**Job:** Take documents/notes/reports with variable structure and turn them into a defined table, action register or evidence summary while preserving a route back to the source.

**Why it belongs:** Common finance/admin friction; AI is useful but extraction errors make verification essential; demonstrates the Ikhaya method particularly well.

**Boundary:** This is not “upload an invoice and trust the extracted figures”. The product must teach source-linked extraction and efficient checking. Sensitive/confidential workplace data requires the user to follow employer policy and approved-tool requirements.

**Checks should include:** source reference for every material item; explicit “not stated” rather than inference; numerical spot-checking or full checking where consequence requires it; missing/ambiguous field flags; reconciliation/completeness checks.

## Why meeting notes are not in the paid core

Claude ranked meeting-notes-to-actions first on frequency and visible pain. However, native AI meeting products and connectors increasingly perform summarisation/action extraction. This makes it a strong free demonstration or lead-magnet workflow, but a weaker anchor for willingness to pay.

## Why business-case drafting is not initially core

AI drafting is heavily commoditised. A business-case example may fit inside the “Challenge My Work” workflow, where the value lies in critique and verification rather than generating another first draft.

## Transformation

### Before

- User experiments with AI inconsistently.
- Results can be impressive but generic or unreliable.
- User does not know how much checking is enough.
- Verification can erase much of the time saving.
- Successful chats are difficult to turn into a repeatable method.

### After

The customer has three personally configured, repeatable AI-assisted work procedures and knows:

- what source material is required;
- how to give the AI sufficient context;
- what AI should and should not do;
- how to verify the result efficiently;
- what evidence should be retained;
- when the result is safe enough to use;
- which decision remains theirs;
- how to repeat the procedure next month/week without starting again.

## Product format hypothesis

Do not create a long ebook.

Build an implementation toolkit:

1. Short orientation: AI as junior collaborator, not source of truth.
2. The six-stage Ikhaya framework.
3. Three guided workflow builds using realistic worked examples.
4. Downloadable/checkable workflow templates.
5. Task-specific quality-control checklists.
6. “Build yours” worksheets so customers adapt each workflow to their real role.
7. Failure-mode examples showing plausible-looking bad AI output and how to catch it.
8. A final personal AI working-method sheet/playbook.

The product should require doing, not merely reading.

## Hormozi value-equation assessment

### Dream outcome

Higher confidence using AI on consequential work, with repeatable time savings and less fear of embarrassing errors.

### Perceived likelihood of achievement

Increase through worked examples, before/after demonstrations, explicit checks, and a small number of workflows rather than broad promises.

### Time delay

Customer should achieve a useful first workflow in the first sitting. Avoid a long theory module before the first result.

### Effort and sacrifice

No specialist automation platform, coding, or paid Microsoft Business account should be required for Product 1. Customer uses a general-purpose AI tool they already have access to, subject to workplace policy.

## Preliminary pricing logic

Do not price yet from competitor PDFs. Validate outcome value first.

Initial hypothesis for testing: this should sit above commodity £3–£15 prompt packs because it is an implementation system, but below formal professional training/course pricing until Ikhaya has proof and testimonials. A beta/founding-customer price can be used to obtain evidence before a permanent price is set.

## Proof required before full build

Before investing heavily, validate:

1. At least 5–10 target users recognise the verification/repeatability problem without being led to the answer.
2. At least three say one or more proposed jobs is sufficiently painful/frequent to want a structured solution.
3. We can demonstrate measurable improvement on realistic test cases: time, error detection, output quality or confidence.
4. The Checks framework catches failure modes that a normal “good prompt” does not adequately address.
5. At least a small number of target customers demonstrate willingness to pay, ideally via a beta/pre-sale rather than survey intent alone.

## Free vs paid boundary

**Free content:** meeting-notes example; basic “AI is not a source of truth” education; individual prompting techniques; simple demonstrations; articles explaining common AI failure modes.

**Paid product:** complete repeatable procedures; worked finance/admin examples; source/evidence discipline; task-specific verification checklists; failure-mode training; reusable templates; guided adaptation to the customer’s own work.

## Naming

“AI Workday System” is retired as a customer-facing name for now. It is too close to generic AI-productivity positioning.

Do not name the product until the proposition and customer language have been validated. Working internal folder name: `ai-quality-system`.

## Next decision gate

Do **not** start producing the finished product yet.

Next phase: design a lean validation test around the three jobs above, including realistic sample tasks, success measures and a short target-user discovery script. Then test whether the Checks layer creates enough additional value to support a paid offer.

## Research basis

This proposition responds to Claude’s 20 August 2026 market research in `research/ai-workday-system/market-research.md`. In particular: prompt packs are commoditised; official vendors increasingly provide free prompting/workflow guidance and connectors; verification burden is strongly evidenced; finance/admin is comparatively under-served; and the research recommendation was to modify and narrow rather than abandon.