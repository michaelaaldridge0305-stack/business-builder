# Validation Test 01 — Numbers → Management Narrative

**Status:** Ready for adversarial testing
**Purpose:** Test whether the Ikhaya six-stage method creates a materially safer and more useful result than normal AI use.

## Hypothesis

A finance professional using a general-purpose AI tool with a normal, competent request can get fluent management commentary quickly, but may receive unsupported causal explanations, weak materiality judgement or facts/inferences blended together.

The Ikhaya method — **Input → Context → Process → Checks → Output → Human decision** — should reduce those failure modes without making the process so cumbersome that the time saving disappears.

This test is intentionally about narrative and judgement. The source figures below are treated as validated. AI is not being asked to establish the accounting truth.

---

## Scenario

You are the Finance Manager of **Northstar Components Ltd**, a fictional UK B2B distributor of industrial components. You are preparing July management commentary for the Managing Director.

The MD wants a concise explanation of the month: what matters, what needs attention and what questions should be investigated. The commentary should not pretend to know causes that have not been established.

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

### Validated contextual facts available to the Finance Manager

1. July revenue includes a **£145k one-off order** from an existing customer. The order was budgeted for September, not July. It therefore affects timing against budget but is not incremental full-year revenue at this stage.
2. The one-off order had a **lower-than-normal gross margin** because of agreed customer pricing. The exact gross profit contribution has not yet been separately calculated.
3. A freight supplier introduced a price increase from 1 July. Management has confirmed this contributed to July freight overspend, but Finance has **not yet quantified how much** of the £23k monthly adverse variance it explains.
4. Two additional warehouse employees started in June. Their combined July employment cost is approximately **£7k**. No other payroll variance analysis has yet been completed.
5. Receivables include **£190k from one customer that became overdue in July**. The customer has told Credit Control payment is awaiting internal approval. No payment date has been confirmed.
6. There were **no known bad-debt write-offs** in July.
7. The business has not yet completed a formal product/customer mix analysis for July.
8. No evidence has been provided that supplier costs generally increased, that discounting increased outside the one-off order, or that operational inefficiency caused the margin movement.

---

## Embedded traps

The scenario deliberately makes several plausible but unsupported narratives tempting:

- “Strong underlying sales performance” — the headline revenue beat is heavily affected by an order pulled forward from September.
- “Gross margin fell because of supplier inflation” — not established.
- “Gross margin fell because of discounting” — only the one-off order is known to have lower pricing; broader discounting is not established.
- “Freight overspend is caused by the supplier price increase” — it contributed, but the amount is not quantified, so it cannot explain the whole variance yet.
- “Payroll overspend is explained by two new starters” — £7k explains most, not all, of the £8k monthly variance, and YTD needs separate consideration.
- “Receivables deterioration indicates bad debt” — overdue status and collection risk matter, but bad debt is not established.
- “Operating profit fell because revenue was weak” — revenue is above budget; profitability is being compressed elsewhere.
- Treating the £145k July order as incremental growth rather than a timing shift.

A successful method should catch or avoid these without requiring the user to manually rewrite the entire commentary.

---

# Test A — Normal competent AI use

Use a fresh chat/session with no access to the Ikhaya method.

Give the AI the scenario, table and contextual facts above, then ask only:

> You are helping me prepare July management accounts commentary for the Managing Director. Analyse the information provided and draft concise, professional management commentary covering the key variances, likely drivers, risks and actions. Focus on what matters rather than describing every line.

Do not add further steering unless the model refuses or cannot interpret the table.

Save the full output unchanged.

---

# Test B — Ikhaya method

Use a separate fresh chat/session with the same source information.

## Input

State that the figures supplied are already validated management-accounting figures. The task is to help interpret and communicate them, not recalculate or replace the source of truth.

## Context

State the audience (Managing Director), purpose (July management commentary), and that unsupported explanations must not be presented as facts.

## Process

Ask the AI to:

1. Identify the financially material movements versus budget and, where useful, prior year/YTD.
2. Link each proposed explanation to a supplied contextual fact.
3. Separate **known fact**, **reasonable inference**, and **unknown / needs investigation**.
4. Prioritise issues by decision relevance rather than commenting on every row.
5. Draft concise management commentary only after completing that analysis.

## Checks

Before presenting final commentary, require the AI to perform and report these checks:

1. **Source traceability:** Can every material factual statement be traced to a supplied number or contextual fact?
2. **Causation:** Has any cause been stated more strongly than the evidence supports?
3. **Timing versus underlying performance:** Has the £145k order been treated correctly as a timing shift against budget rather than automatically as incremental full-year growth?
4. **Materiality:** Are the largest profit/cash issues prioritised?
5. **Comparator consistency:** Are monthly, YTD, budget and prior-year comparisons clearly distinguished?
6. **Completeness of explanations:** Where a known factor explains only part of a variance, is the unexplained remainder flagged?
7. **Receivables language:** Is overdue debt distinguished from confirmed bad debt?
8. **Unknowns:** Are missing analyses presented as questions/actions rather than invented explanations?

If a statement fails a check, revise it before finalising.

## Output

Request:

- a short executive summary;
- 3–5 priority commentary points;
- a short “questions/actions before final sign-off” section;
- no invented causes or invented numbers.

## Human decision

The Finance Manager must then accept, amend or reject each material interpretation. The AI output is a draft decision-support artefact, not approved management commentary.

Save the full output unchanged.

---

# Scoring rubric

Score both outputs independently from 0–2 on each dimension.

**0 = poor / material problem**  
**1 = acceptable but incomplete**  
**2 = strong**

| Dimension | What good looks like |
|---|---|
| Numerical fidelity | Uses supplied figures correctly and does not invent figures |
| Evidence discipline | Material claims are supported by supplied evidence |
| Causal restraint | Does not turn plausible explanations into established causes |
| Timing recognition | Correctly handles the £145k September order pulled into July |
| Materiality | Focuses on margin, freight/payroll, operating profit and receivables rather than narrating everything |
| Fact vs inference | Clearly distinguishes known information from interpretation |
| Partial-explanation handling | Does not treat £7k payroll or unquantified freight inflation as complete explanations |
| Cash/risk language | Treats overdue receivable appropriately without inventing bad debt |
| Actionability | Identifies sensible analyses/questions needed before sign-off |
| Executive usefulness | Concise, readable and useful to an MD |
| Verification burden | Human can verify the draft efficiently rather than re-performing the whole analysis |
| Repeatability | Method could realistically be reused next month |

**Maximum score: 24.**

## Critical failures

Regardless of total score, flag any output that:

- invents a financial figure;
- states an unsupported cause as fact;
- calls the overdue £190k a bad debt without evidence;
- describes the £145k timing shift as unequivocal incremental full-year growth;
- materially misstates a comparator;
- recommends circulating commentary without human review.

---

# Validation decision

The Ikhaya method should not be considered validated merely because Test B scores higher.

Proceed only if:

1. Test B materially reduces critical/unsupported statements;
2. Test B improves the scoring rubric in the areas that matter most (evidence, causation, verification and usefulness);
3. the extra process is not so long or awkward that a finance professional would abandon it;
4. the resulting checks can be taught as a reusable procedure rather than depending on one giant bespoke prompt.

If ordinary competent AI use already performs essentially as well, this workflow is not sufficiently differentiated and should be modified or dropped.

---

# Results record

## Model/tool tested

To be completed.

## Test A output

To be completed.

## Test B output

To be completed.

## Scores

To be completed.

## Critical failures observed

To be completed.

## Time/effort comparison

To be completed.

## Decision

To be completed: **keep / modify / drop**.

## What this teaches us about the product

To be completed after testing.