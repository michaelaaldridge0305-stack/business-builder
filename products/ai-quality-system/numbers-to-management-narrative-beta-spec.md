# Numbers to Management Narrative - Internal Beta Specification

**Status:** Internal specification complete, awaiting independent human validation
**Target price hypothesis:** £18 to £20
**Workflow:** Turn validated management-account numbers and known business context into concise, decision-useful management commentary with explicit verification controls.

## 1. Customer and job to be done

Primary beta user: UK finance professionals who already prepare monthly management accounts and use, or are willing to use, a general-purpose AI assistant.

Job to be done: reduce the time and cognitive load of turning validated numbers and known context into management-ready narrative without delegating professional judgement or sign-off to AI.

The product does not calculate the accounts, replace variance analysis, provide accounting advice, or promise error-free output.

## 2. Minimum beta deliverable

The beta should be deliberately narrow. It contains:

1. A short start-here guide explaining the workflow and boundaries.
2. An editable Numbers Input Template.
3. An editable Context and Evidence Template.
4. A reusable AI instruction that produces an executive summary, priority commentary and actions/questions before sign-off.
5. A House Style Template so users can specify wording conventions and tone.
6. Three worked failure examples showing plausible AI output that should not be accepted.
7. A one-page Final Verification Checklist.
8. A short Safe Data and Human Sign-off note.
9. A self-service troubleshooting section limited to common workflow problems.

No videos, calls, bespoke implementation, spreadsheet model or software integration are required for the minimum beta.

## 3. Editable input template

### Reporting context
- Company / fictional identifier:
- Reporting period:
- Audience:
- Purpose of commentary:
- Materiality / focus threshold if used:

### Validated numbers
For each metric provide, where relevant:
- Metric name
- Current-period actual
- Current-period budget or forecast
- Prior-year comparator
- YTD actual
- YTD budget or forecast
- Units (£, £000, %, days, units etc.)

### Known evidence
For each known factor:
- Fact supported by evidence
- Amount, if quantified
- Period affected
- Whether it explains all or only part of a variance
- Whether it is timing/phasing, recurring, one-off, classification-related or not yet known

### Unknowns
List material movements for which a complete explanation has not yet been established. Do not invent a cause to fill a gap.

## 4. Context and evidence control

Before drafting, the AI must separate supplied information into:

- validated figures;
- validated contextual facts;
- management-approved assumptions, if any;
- unresolved unknowns.

It must not promote an unknown or an indicator into a fact. Where a known item explains only part of a variance, wording must say so and identify the residual as unresolved where material.

## 5. Reusable AI instruction

Role: Act as an experienced UK management-accounting reviewer. Using only the validated figures, context and house-style rules supplied, prepare concise management commentary for the stated audience.

Output:
1. Short executive summary.
2. Three to five priority commentary points, ranked by management relevance rather than table order.
3. Questions/actions required before sign-off.

Controls:
- Recalculate material variances and percentage movements before describing them.
- Check favourable/adverse direction, comparator and reporting period.
- Never state a causal explanation more strongly than the supplied evidence supports.
- Distinguish full explanations from partial explanations.
- Identify timing, phasing, classification and one-off effects where supplied.
- Do not invent causes, trends, operational events or commercial facts.
- Describe risks as risks or indicators unless an outcome is confirmed.
- Preserve clear conclusions where evidence is strong rather than adding unnecessary caveats.
- Give a useful follow-up action for material unresolved items.
- Apply the supplied house style.
- Finish by identifying any statement that still needs human verification.

## 6. House Style Template

Users can define:
- UK English: yes/no
- Audience seniority:
- Tone: concise / explanatory / board-style / other
- Preferred variance format, e.g. £36k adverse or £36k below budget
- Percentage convention, e.g. 0.6% rather than 0.6 percentage points
- Unit convention, e.g. inventory days: 68 days
- Terms to avoid:
- Preferred treatment of incomplete analysis, e.g. explain why analysis remains outstanding rather than implying it was omitted
- Maximum commentary length:

Default beta style: professional, concise UK English; specific about evidence; confident where facts are known; explicit but non-defensive about material unknowns.

## 7. Failure examples

### Failure 1: invented cause
Weak AI output: "Revenue was below budget because customer demand softened in August."
Why it fails: a revenue shortfall does not establish weaker demand. If the supplied evidence only identifies a delayed order, the commentary must state the known timing effect and avoid inventing a broader demand trend.

### Failure 2: partial explanation presented as complete
Weak AI output: "Payroll was £12k over budget due to the new sales manager."
Why it fails: if the new manager accounts for only £6k, half of the variance remains unexplained. Better wording quantifies the known £6k contribution and states that the remaining variance requires payroll analysis.

### Failure 3: indicator converted into confirmed loss
Weak AI output: "£85k of old inventory must be written off."
Why it fails: ageing/no recent sales is a risk indicator, not evidence of impairment by itself. Commentary should flag the stock for review and distinguish possible markdown or impairment from a confirmed accounting outcome.

### Failure 4: timing benefit mistaken for structural improvement
Weak AI output: "Gross margin has permanently improved due to better supplier pricing."
Why it fails: a one-period rebate or phasing benefit cannot establish a permanent improvement, particularly where no evidence of general supplier price reduction exists.

## 8. Final Verification Checklist

Before using the commentary, the finance professional confirms:

- [ ] Material figures and variances agree to the validated source data.
- [ ] Percentages, units, periods and comparators are correct.
- [ ] Favourable/adverse language is directionally correct.
- [ ] Every causal statement is supported by supplied evidence.
- [ ] Partial explanations are not presented as complete explanations.
- [ ] Timing, phasing, classification and one-off effects are described correctly.
- [ ] No new business fact, trend or cause has been invented by the AI.
- [ ] Risks and indicators have not been converted into confirmed outcomes.
- [ ] Material unknowns are visible and have a useful follow-up action.
- [ ] Commentary prioritises matters relevant to management decisions.
- [ ] House style and terminology are appropriate for the intended audience.
- [ ] A finance professional has applied judgement and accepts responsibility for final sign-off.

## 9. Safe-data boundary

The toolkit should encourage users to follow their employer's information-security, privacy and AI-use policies. Users should not paste confidential, personal, commercially sensitive or client information into an AI service unless their organisation has approved that service and the proposed use. Where approval is uncertain, use anonymised or fictionalised information and remove identifiers.

The beta does not certify any AI service as suitable for confidential financial information. Data-handling requirements depend on the user's organisation, contract, configuration and applicable policies.

## 10. Human sign-off boundary

AI output is a drafting and challenge aid, not an accounting record or professional sign-off. The user remains responsible for validating numbers, assessing accounting treatment, judging materiality, evaluating evidence, deciding what management should be told and approving the final commentary.

## 11. Self-service support boundary

Included support content should cover only:
- how to structure inputs;
- what to do when the AI invents a cause;
- how to handle incomplete variance explanations;
- how to tighten overly verbose output;
- how to apply house style;
- how to rerun the verification check.

Not included:
- calls or meetings;
- review of a customer's real management accounts;
- bespoke prompt engineering;
- accounting advice;
- AI platform setup, licensing or security configuration;
- integration with Excel, ERP, reporting or BI systems.

If the product routinely requires those services to create value, the self-service proposition has failed its validation gate.

## 12. Commercial hypothesis and validation gate

The £18 to £20 price is a hypothesis supported only by the owner's two participant responses (£20 and £18). It is not independent willingness-to-pay evidence.

Before public build/listing, require:
1. A clean fresh-session test where the generating model has not seen evaluator material.
2. At least two independent UK finance target-user tests.
3. Independent evaluation of resulting artefacts.
4. At least one independent timed result showing net effort saving.
5. A real beta purchase/pre-sale signal before public launch.

Stop or reposition if a simple free instruction performs equally well, independent users do not save time, critical errors persist, users will not pay, or support requirements turn the product into a service.

## 13. Internal QA conclusion

Scope has been deliberately reduced to one recurring finance job. Paid value is intended to come from the structured evidence boundary, reusable templates, finance-specific failure patterns, house-style control and final verification procedure rather than from a generic prompt alone.

The specification is internally coherent and buildable without new spend. The unresolved commercial risk is not product completeness but independent evidence that target users experience enough incremental value over a free prompt to pay for the toolkit. That risk must be tested rather than assumed.