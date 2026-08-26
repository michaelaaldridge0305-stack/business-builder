# Numbers to Management Narrative

## Turn validated management accounts into management-ready commentary without letting AI invent the story

**Internal build status:** Customer pack v1, prepared for QA

## Start here

This toolkit is for finance professionals who already have validated management-account numbers and known business context, but want a faster, more controlled way to turn them into concise management commentary using a general-purpose AI assistant.

It is not an accounting model and it does not perform month-end close, variance investigation or professional sign-off for you. Its purpose is narrower: help you draft the narrative once the underlying numbers and evidence are ready.

### The workflow

1. Complete the Numbers Input Template using validated figures.
2. Complete the Context and Evidence Template. Separate what you know from what is still unknown.
3. Set your House Style once, then reuse it each month.
4. Paste the completed inputs, house style and AI instruction into your approved AI assistant.
5. Review the draft using the Final Verification Checklist.
6. Correct anything unsupported, unclear or incomplete before sign-off.

The key rule is simple: **AI may help write the commentary. It may not invent the explanation.**

---

# 1. Numbers Input Template

Copy and complete this section for the reporting period.

## Reporting context

- Company or anonymised identifier:
- Reporting period:
- Audience:
- Purpose of commentary:
- Materiality or focus threshold, if used:

## Validated numbers

| Metric | Current actual | Budget / forecast | Prior year | YTD actual | YTD budget / forecast | Unit |
|---|---:|---:|---:|---:|---:|---|
| Revenue | | | | | | £ / £000 |
| Gross profit | | | | | | £ / £000 |
| Gross margin | | | | | | % |
| Payroll | | | | | | £ / £000 |
| Other operating costs | | | | | | £ / £000 |
| Operating profit / EBITDA | | | | | | £ / £000 |
| Cash | | | | | | £ / £000 |
| Inventory / WIP | | | | | | £ / £000 |
| Other material KPI | | | | | | |

Delete rows that are irrelevant and add metrics that matter to your management pack.

**Input rule:** use figures you have already validated. This toolkit is not a substitute for reconciling the source accounts.

---

# 2. Context and Evidence Template

For each material movement, record what the business actually knows before asking AI to explain it.

| Area / variance | Supported fact | Quantified amount | Period affected | Full or partial explanation? | Type | What remains unknown? |
|---|---|---:|---|---|---|---|
| | | | | Full / Partial | Timing / phasing / recurring / one-off / classification / other | |
| | | | | | |
| | | | | | |

## Management-approved assumptions, if any

List assumptions separately from facts. If none, write **None**.

- 

## Material unknowns

List movements where investigation is incomplete. Do not supply a likely cause simply to make the commentary sound finished.

- 

### Evidence test

Before moving on, ask:

- Do I know this, or am I inferring it from the numbers?
- Does the evidence explain the whole variance or only part of it?
- Is this a timing or one-off effect that could be mistaken for a trend?
- Is an apparent risk actually a confirmed outcome?
- If analysis is incomplete, can I explain what remains to be done and why?

---

# 3. House Style Template

Complete this once and adjust when your audience changes.

- UK English: Yes / No
- Audience seniority:
- Tone: Concise / Explanatory / Board-style / Other
- Preferred variance wording: e.g. `£36k below budget` or `£36k adverse`
- Percentage convention: e.g. `0.6%` rather than `0.6 percentage points`
- Unit convention: e.g. `68 days` rather than `68`
- Terms or phrases to avoid:
- Treatment of incomplete analysis:
- Maximum commentary length:
- Other house rules:

### Suggested default

Professional, concise UK English. Prioritise matters relevant to management decisions. Be confident where evidence is clear and precise where analysis is incomplete. Do not make incomplete work sound like an omission: where appropriate, explain what has not yet been analysed and the reason or next action.

---

# 4. Reusable AI Instruction

Paste the instruction below into your approved AI assistant after the completed Numbers Input, Context and Evidence, and House Style sections.

## Prompt

Act as an experienced UK management-accounting reviewer.

Using only the validated figures, contextual facts, approved assumptions and house-style rules I have supplied, prepare concise management commentary for the stated audience.

Produce:

1. A short executive summary.
2. Three to five priority commentary points ranked by management relevance, not by the order of the source table.
3. A short questions and actions before sign-off section.

Before drafting, separate the supplied information into:

- validated figures;
- validated contextual facts;
- management-approved assumptions;
- unresolved unknowns.

Then apply these controls:

- Recalculate material variances and percentage movements before describing them.
- Check the comparator, reporting period, unit and favourable/adverse direction.
- Do not state a causal explanation more strongly than the evidence supports.
- Distinguish a full explanation from a partial explanation. If a known item explains only part of a material variance, quantify the known part where possible and identify the residual as unresolved.
- Identify supplied timing, phasing, classification and one-off effects so they are not mistaken for structural trends.
- Do not invent causes, trends, operational events, commercial facts or management decisions.
- Describe risks and indicators as risks or indicators unless an outcome is confirmed.
- Do not weaken a clear, evidence-backed conclusion with unnecessary caveats.
- For material unknowns, state a useful follow-up action. Where the supplied context explains why analysis remains outstanding, make that clear rather than making the work sound forgotten or omitted.
- Apply the supplied house style and terminology.
- Keep the commentary decision-useful and proportionate. Do not narrate every line of the accounts.

After drafting, run a verification pass against the supplied information. Finish with a separate section headed **Human verification required** containing only statements or calculations that still require a finance professional to check. If none are identified, state that no additional items were identified by the AI review, but that final professional sign-off remains with the user.

Do not provide accounting advice or make an accounting judgement that has not been supplied by the finance professional.

---

# 5. Worked Failure Examples

These examples show why a fluent AI draft can still be unsafe to use without review.

## Failure 1: invented cause

**Numbers:** Revenue is £70k below budget.

**Evidence supplied:** A £92k customer order included in the August budget was delayed by the customer and shipped on 3 September. There is no evidence of a cancellation or broader demand reduction.

**Do not accept:**

> Revenue was below budget because customer demand softened in August.

**Why it fails:** The numbers do not establish weaker demand. The supplied evidence supports a timing explanation for a specific order, not a general commercial trend.

**Better:**

> August revenue was £70k below budget. A £92k customer order included in the August budget was delayed at the customer's request and shipped on 3 September, indicating a material timing effect rather than a cancelled sale. The September forecast should be refreshed for the shifted order.

## Failure 2: partial explanation presented as complete

**Numbers:** Payroll is £12k above budget.

**Evidence supplied:** A new sales manager contributed approximately £6k of August employment cost. The remaining payroll variance has not yet been analysed.

**Do not accept:**

> Payroll was £12k over budget due to the new sales manager.

**Why it fails:** Only £6k of the £12k variance is supported by the evidence. The statement turns a partial explanation into a complete one.

**Better:**

> Payroll was £12k above budget, of which approximately £6k relates to the new sales manager. The remaining £6k has not yet been explained because the detailed payroll variance analysis is still to be completed and should be resolved before final sign-off.

## Failure 3: a risk turned into a confirmed loss

**Evidence supplied:** £85k of older accessories has had no sale in the last 120 days. Operations is reviewing whether this is seasonal, excess stock or stock requiring markdown. No impairment decision has been made.

**Do not accept:**

> £85k of old inventory must be written off.

**Why it fails:** Ageing is a risk indicator. It is not, by itself, evidence that the entire balance is impaired or must be written off.

**Better:**

> £85k of older accessories has had no sale in the last 120 days and requires management attention. Operations is reviewing whether this reflects seasonality, excess stock or a potential markdown requirement. No impairment conclusion has yet been reached.

## Failure 4: temporary benefit described as structural improvement

**Evidence supplied:** Gross margin benefited from approximately £11k of supplier rebate income in the month. The rebate was budgeted across the year. There is no evidence of a general supplier price reduction or permanent mix improvement.

**Do not accept:**

> Gross margin has permanently improved due to better supplier pricing.

**Why it fails:** A rebate or phasing effect in one period does not prove a permanent margin improvement, and the stated cause was not supplied.

**Better:**

> August gross margin benefited from approximately £11k of supplier rebate income. As the rebate was budgeted across the year rather than specifically in August, this is partly a phasing benefit and should not be treated as evidence of a permanent improvement in underlying margin.

---

# 6. Final Verification Checklist

Complete this before using the commentary as the basis of a management pack.

- [ ] Material figures and variances agree to the validated source data.
- [ ] Percentages, units, periods and comparators are correct.
- [ ] Favourable and adverse wording is directionally correct.
- [ ] Every causal statement is supported by supplied evidence.
- [ ] Partial explanations have not been presented as complete explanations.
- [ ] Timing, phasing, classification and one-off effects are described correctly.
- [ ] The AI has not introduced a new business fact, trend or cause.
- [ ] Risks and indicators have not been converted into confirmed outcomes.
- [ ] Material unknowns are visible and have a useful follow-up action.
- [ ] Where analysis is incomplete, the wording explains the status appropriately rather than implying the work was simply omitted.
- [ ] Commentary prioritises matters relevant to management decisions.
- [ ] House style, terminology and units suit the intended audience.
- [ ] I have applied my own professional judgement and accept responsibility for final sign-off.

---

# 7. Troubleshooting

## The AI invented a cause

Delete or challenge the sentence. Return to the Context and Evidence Template and check whether the cause was actually supplied as a supported fact. If not, instruct the AI to describe the variance without assigning that cause and to identify the explanation as unresolved where material.

## A known item explains only part of the variance

Give the AI both numbers: the total variance and the quantified known factor. Explicitly label the explanation **partial**. Ask it to quantify the residual and identify the remaining analysis or action.

## The draft is too long

Set a maximum length in House Style. Ask for three to five issues ranked by management relevance. Do not ask the AI to comment on every account line.

## The draft sounds hesitant

Check whether the evidence is genuinely uncertain. If a fact is validated, tell the AI to state it clearly. Reserve caveats for actual uncertainty rather than adding words such as `may`, `could` and `potentially` to established facts.

## The draft sounds too certain

Look for causal words such as `because`, `due to`, `driven by`, `reflects` and `will`. Check each one against the evidence supplied. Replace unsupported certainty with the known fact, the limit of the evidence and the next action.

## The wording does not sound like your management pack

Tighten the House Style Template. Add your preferred variance wording, unit conventions, phrases to avoid, audience and maximum length. Re-run the draft rather than manually correcting the same style issues every month.

## Analysis is still incomplete

Do not ask AI to fill the gap. State what is known, what remains outstanding, why it remains outstanding if that context is known, and what will resolve it. This is more credible than an invented explanation and more professional than wording that makes the analysis appear forgotten.

## You changed the inputs after the first draft

Re-run the verification pass against the updated source information. Do not assume an earlier conclusion still holds.

---

# 8. Safe Data and Human Sign-off

Use this toolkit only in line with your organisation's information-security, privacy and AI-use policies.

Do not paste confidential, personal, commercially sensitive or client information into an AI service unless your organisation has approved that service and the proposed use. If approval is uncertain, anonymise or fictionalise the information and remove identifiers.

This toolkit does not certify ChatGPT, Claude, Copilot or any other AI service as suitable for your organisation's confidential financial data. Security and data-handling requirements depend on your employer, service configuration, contracts and policies.

AI output is a drafting and challenge aid. It is not an accounting record, accounting advice or professional sign-off.

You remain responsible for validating the underlying numbers, assessing accounting treatment, judging materiality, evaluating evidence, deciding what management should be told and approving the final commentary.

---

# 9. What this toolkit does not include

This is a self-service digital toolkit. It does not include:

- review of your real management accounts;
- calls or meetings;
- bespoke prompt engineering;
- accounting advice;
- AI platform setup or licensing advice;
- security configuration;
- Excel, ERP, Power BI or other system integration.

If you need any of those services, they sit outside this product.
