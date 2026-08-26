# Numbers to Management Narrative - QA 01

**Date:** 26 August 2026
**Artifact reviewed:** `numbers-to-management-narrative-customer-pack.md`
**Reviewer stance:** sceptical customer, commercial reviewer and finance-quality reviewer

## Result

**PASS WITH MINOR INTERNAL REVISIONS COMPLETED IN BUILD.**

The customer pack is coherent, practical and materially stronger than a generic prompt because it combines a structured evidence boundary, explicit distinction between partial/full explanations, reusable house style, finance-specific failure examples and a final human verification procedure.

## Checks performed

### Finance and numerical logic

- Failure 1: £70k revenue shortfall and £92k delayed order are intentionally not netted into an unsupported conclusion. Wording correctly treats the known order as a material timing effect rather than claiming it mathematically explains the entire movement.
- Failure 2: £12k payroll variance less £6k known new-manager cost leaves £6k unresolved. Correct.
- Failure 3: £85k aged stock is described as a review/risk indicator rather than a confirmed impairment. Correct.
- Failure 4: £11k rebate is treated as a period/phasing benefit and not evidence of permanent supplier-price or mix improvement. Correct.
- Units and comparator controls are explicit.

### Evidence discipline

Pass. The product repeatedly distinguishes validated figures, facts, assumptions and unknowns. It prevents AI from manufacturing explanations and makes residual unexplained variances visible.

### Professional usability

Pass. Workflow is short enough to use monthly. Editable structures are copyable and do not require software beyond a general-purpose AI assistant. The prompt ranks issues by management relevance rather than account-table order.

### Human tone and UK finance style

Pass. UK English is used. Customer-facing prose avoids em dashes. Percentage and unit conventions can be customised. Incomplete analysis is framed by status/reason/next action rather than sounding careless.

### Scope and support burden

Pass. No calls, bespoke account review, implementation or accounting advice are promised. The self-service boundary is explicit.

### Safety and claims

Pass. The pack does not claim independent validation, guaranteed time savings or error-free AI. It explicitly requires organisational approval for use of sensitive financial information and preserves human professional sign-off.

## Defects considered and resolution

1. **Risk: customer could mistake the toolkit for variance analysis.** Resolved through repeated statement that inputs must already be validated and investigation remains the finance professional's responsibility.
2. **Risk: verification section could imply AI certifies its own output.** Resolved by requiring a separate human checklist and wording that AI identification of no additional issues does not replace sign-off.
3. **Risk: incomplete analysis could read as sloppy work.** Resolved by adding explicit guidance to state why analysis remains outstanding where that context is known and identify the resolving action.
4. **Risk: generic-prompt commoditisation.** Mitigated, not eliminated. Paid value is the reusable operating method, examples and evidence controls rather than access to a secret prompt. This remains a commercial risk and must not be disguised.

## Remaining material commercial risk

Independent willingness-to-pay has not been established because the owner explicitly chose to progress without further human validation. This does not prevent the authorised build, but customer-facing claims must not imply independent validation.

## QA conclusion

The underlying written product is ready to move from BUILD to PACKAGING. Visual/layout QA remains required once customer files are rendered into their final delivery format. Listing copy may now be prepared, but external publication remains an owner gate.
