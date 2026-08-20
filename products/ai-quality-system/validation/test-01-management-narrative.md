# Validation Test 01 v2 — Numbers → Management Narrative

**Status:** Redesigned after adversarial review; ready for controlled testing
**Purpose:** Determine whether the Ikhaya method adds material value beyond both ordinary AI use and the cheapest plausible free improvement.

## Hypothesis

A reusable finance-specific quality method should improve the reliability and usefulness of AI-assisted management commentary **beyond what a competent user can obtain by adding one sensible uncertainty instruction**, while keeping the human verification burden proportionate.

The Ikhaya method is:

**Input → Context → Process → Checks → Output → Human decision**

This test does not ask AI to establish accounting truth. Source figures are treated as validated. The task is interpretation, challenge and communication.

---

## Scenario

You are the Finance Manager of **Northstar Components Ltd**, a fictional UK B2B distributor of industrial components. You are preparing July management commentary for the Managing Director.

The MD wants a concise explanation of the month: what matters, what needs attention and what questions should be investigated. Commentary must be decisive where evidence is clear and appropriately qualified where it is not.

### July management data — £000 unless stated

| Metric | July Actual | July Budget | July LY | YTD Actual | YTD Budget |
|---|---:|---:|---:|---:|---:|
| Revenue | 1,260 | 1,200 | 1,145 | 8,310 | 8,050 |
| Gross profit | 365 | 372 | 355 | 2,475 | 2,496 |
| Gross margin | 29.0% | 31.0% | 31.0% | 29.8% | 31.0% |
| Payroll | 188 | 180 | 171 | 1,286 | 1,245 |
| Freight | 71 | 48 | 45 | 390 | 326 |
| Other operating costs | 82 | 84 | 79 | 568 | 574 |
| Operating profit | 24 | 60 | 60 | 231 | 351 |
| Closing receivables | 1,610 | 1,350 | 1,290 | — | — |
| Debtor days | 47 | 40 | 39 | — | — |

### Validated contextual facts

1. July revenue includes a **£145k one-off order** from an existing customer. It was budgeted for September, not July. It affects timing against budget and is not currently incremental full-year revenue.
2. The one-off order had a **lower-than-normal gross margin** because of agreed customer pricing. Its exact gross profit contribution has not yet been separately calculated.
3. A freight supplier introduced a price increase from 1 July. Management has confirmed it contributed to July freight overspend, but Finance has **not quantified how much** of the £23k monthly adverse variance it explains.
4. Two additional warehouse employees started in June. Their combined July employment cost is approximately **£7k**. No other payroll variance analysis has yet been completed.
5. Receivables include **£190k from one customer that became overdue in July**. Credit Control has been told payment is awaiting the customer's internal approval. No payment date has been confirmed.
6. There were **no known bad-debt write-offs** in July.
7. The business has not yet completed formal product/customer mix analysis for July.
8. No evidence has been provided that supplier costs generally increased, that discounting increased outside the one-off order, or that operational inefficiency caused the margin movement.

### Hidden evaluation traps

These are for the evaluator only. **Do not provide this section to the model being tested.**

- Treating the headline revenue beat as proof of strong underlying July sales.
- Treating the £145k timing shift as incremental full-year growth.
- Attributing the gross-margin decline to general supplier inflation or broad discounting without evidence.
- Treating the freight price rise as explaining all of the £23k monthly adverse variance.
- Treating the £7k new-starter cost as explaining all payroll variance, including YTD.
- Treating overdue receivables as confirmed bad debt.
- Explaining weak operating profit through weak revenue when revenue is above budget.
- Missing or reversing favourable/adverse variance direction.
- Becoming so cautious that clear facts and clear movements are buried in caveats.

---

# Experimental design

Run **three conditions**. Each condition receives the same scenario, data and validated contextual facts, but never the hidden evaluation traps.

Use fresh sessions with no shared context between conditions.

## Condition A — Ordinary competent use

Prompt:

> You are helping me prepare July management accounts commentary for the Managing Director. Analyse the information provided and draft concise, professional management commentary covering the key variances, likely drivers, risks and actions. Focus on what matters rather than describing every line.

This represents a reasonable user who knows how to ask for the job but has not added a specific quality-control instruction.

## Condition A2 — Cheapest plausible free improvement

Use the exact Condition A prompt plus only:

> Only state a cause when the information provided supports it. Where the cause is uncertain, say so and identify what should be checked rather than guessing.

No other quality framework is supplied.

This is the key commercial control. If A2 captures most of B's benefit, a paid Ikhaya method has weak marginal value for this job.

## Condition B — Ikhaya generic method

The method must remain reusable across different management packs. **Do not mention Northstar-specific risks, figures, customers, timing events, freight, payroll or receivables in the Checks instructions.**

### Input

Tell the AI which information is the validated source of truth and what it is being asked to do with that information. It must not silently replace validated source data with its own assumptions.

### Context

Specify audience, purpose, decision/use case, relevant business context and the required level of brevity. State that the output must be decisive where evidence is clear and explicit about uncertainty where it is not.

### Process

Ask the AI to:

1. identify material movements and relationships in the supplied information;
2. distinguish observed facts from explanations and hypotheses;
3. prioritise what matters to the intended decision-maker;
4. identify gaps that prevent a confident explanation;
5. draft only after completing that analysis.

### Checks — generic finance-commentary quality controls

Before finalising, require the AI to check:

1. **Numerical fidelity:** Are quoted figures, percentages, periods and directions consistent with the supplied source?
2. **Comparator clarity:** Is it always clear whether a statement refers to budget, prior period/prior year or cumulative performance?
3. **Evidence-to-claim strength:** Is each explanation no stronger than the evidence supporting it?
4. **Reconciliation of explanation:** Where a known factor explains only part of a movement, is the remaining unexplained amount or uncertainty acknowledged?
5. **Timing versus underlying economics:** Could a movement reflect timing, phasing, classification or one-off effects rather than underlying performance?
6. **Materiality and decision relevance:** Does the commentary focus on matters that could change a management decision or warrant action?
7. **Risk-language precision:** Are accounting, cash, operational and credit risks described without escalating an indicator into a confirmed outcome?
8. **Unsupported inference:** Has the draft introduced any cause, trend or business fact that was not supplied or logically supported?
9. **Usefulness versus caution:** Has uncertainty been handled without burying clear, supported conclusions in unnecessary caveats?
10. **Actionability:** For material unknowns, does the draft identify the minimum useful follow-up analysis or action?

Revise any statement that fails a check before presenting the final draft.

### Output

Request:

- a short executive summary;
- 3–5 priority commentary points;
- a short questions/actions-before-sign-off section;
- no invented causes or invented numbers.

### Human decision

State explicitly that the Finance Manager owns final judgement and sign-off. AI prepares a decision-support draft; it does not approve the commentary.

---

# Replication plan

Do not make a product decision from one attractive output.

Minimum exploratory run:

- **3 fresh runs per condition per model**;
- test on **ChatGPT and Claude** initially;
- add Copilot later if access can be obtained without creating unnecessary cost or using an employer account for this business project.

This gives 18 initial outputs: 3 conditions × 3 runs × 2 models.

Record model/product and date. Where settings such as model version or reasoning mode are visible, record them.

---

# Independent scoring rubric

Score each final output 0–2 on each dimension.

**0 = material weakness**  
**1 = acceptable / mixed**  
**2 = strong**

The evaluator should score the final management artefact, not reward an output merely for visibly following the supplied method.

| Dimension | What good looks like |
|---|---|
| Accuracy | Numbers, percentages, signs/directions and periods are correctly represented |
| Analytical validity | Conclusions follow from the evidence; no material logical leap |
| Explanatory calibration | Clear evidence is stated clearly; uncertain explanations are appropriately qualified |
| Materiality/prioritisation | The MD's attention is directed to the matters that matter most |
| Commercial/management usefulness | Commentary helps a decision-maker understand performance rather than merely describing data |
| Clarity and brevity | Readable, proportionate and not overloaded with process language or caveats |
| Risk judgement | Risks are identified at an appropriate level without exaggeration or false reassurance |
| Action quality | Follow-ups are specific, proportionate and useful |
| Traceability | A finance professional can efficiently trace material statements back to supplied evidence |
| Human verification effort | The draft can be checked materially faster than rebuilding the analysis from scratch |

**Maximum: 20.**

## Critical failures

Flag separately from the score:

- invented financial figure;
- material sign/direction error;
- material comparator error;
- unsupported causal claim presented as established fact;
- timing/phasing item materially misrepresented as underlying/incremental performance;
- risk indicator materially escalated into a confirmed outcome without evidence;
- output is so hedged that it fails to communicate a clear supported conclusion;
- output implies AI rather than the responsible professional should own final sign-off.

---

# Verification-burden measurement

The product hypothesis explicitly depends on saving work, so record this separately from quality score.

For each output, the evaluator records:

1. **Material claims count:** number of statements a Finance Manager would reasonably need to validate before sign-off.
2. **Unsupported/problem claims count:** number requiring correction because the source does not support them.
3. **Traceback friction:** Low / Medium / High — how difficult it is to find the evidence for each material claim in the supplied pack.
4. **Correction effort:** estimated minutes required to turn the draft into sign-off-ready commentary, excluding normal stylistic preference changes.
5. **Discard/rebuild:** Yes/No — would it be quicker or safer to rebuild the commentary rather than repair this output?

For the first human validation round, ask actual target users to time the review/correction task rather than relying solely on estimates.

---

# Blinding

Where practical, remove labels identifying A, A2 and B before human scoring. Randomise output order. The scorer should not know which method generated which artefact.

The person who designed the Ikhaya prompt should not be the sole judge of whether Ikhaya won.

---

# Product decision rules

Do not validate B merely because it has the highest mean score.

## Strong evidence to KEEP the workflow

B must show a repeatable advantage over **A2**, not merely A, in the commercially important areas: analytical validity, calibrated explanation, traceability, risk judgement and verification effort. The advantage must survive multiple runs and not depend on Northstar-specific wording.

## Evidence to MODIFY

B improves reliability but creates excessive length/process overhead, or A2 achieves most of the quality gain. In this case, simplify the method until the marginal benefit per unit of effort is defensible.

## Evidence to DROP from the paid core

A2 performs essentially as well as B across models/runs and has similar verification burden; or B's additional process costs more time than it saves. The job may still be useful free content, but it is not sufficiently differentiated as a paid workflow.

---

# Customer-transfer test — required before commercial validation

Even if B wins this benchmark, the product is **not** validated until a target user can apply the principles to a different management pack without receiving a bespoke answer-key checklist.

Later validation must therefore give a finance professional:

1. the generic six-stage method and generic Checks principles;
2. a new unseen scenario;
3. no pre-written scenario-specific traps;
4. the task of configuring and using the method themselves.

Measure output quality, verification effort and whether they can repeat the procedure without expert intervention.

This is the actual test of whether Ikhaya is teaching a transferable system rather than selling a sophisticated prompt.

---

# Data-handling boundary

All benchmark data is fictional. Real customer testing must instruct participants to use only data they are authorised to provide to the selected AI service and to follow employer/client policies. The product must not imply that a technically possible upload is an authorised upload.

---

# Results record

## Models and run dates

To be completed.

## Condition A outputs

To be completed.

## Condition A2 outputs

To be completed.

## Condition B outputs

To be completed.

## Blind scores

To be completed.

## Critical failures

To be completed.

## Verification-burden results

To be completed.

## Cross-model/run consistency

To be completed.

## Decision

To be completed: **KEEP / MODIFY / DROP FROM PAID CORE**.

## What this teaches us about the product

To be completed after testing.

---

## Revision note

Version 2 incorporates the adversarial review in `claude-review-test-01.md`: adds the A2 commercial control; replaces scenario-specific Checks with generic finance-commentary principles; separates evaluation from method compliance; adds over-hedging and sign/direction failure modes; defines verification-burden measures; introduces replication and blinding; and adds a later customer-transfer test.