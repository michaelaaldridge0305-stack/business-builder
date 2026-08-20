# Adversarial Review of Validation Test 01 — Numbers → Management Narrative

**Reviewer:** Claude (Anthropic)
**Date:** 20 August 2026
**Reviewed file:** `products/ai-quality-system/validation/test-01-management-narrative.md` (commit `1fc17f6`)
**Also read for context:** `products/ai-quality-system/product-1-proposition.md`, `research/ai-workday-system/market-research.md`
**Test was NOT run.** This is a design review only, per instruction.

---

## Verdict

**REDESIGN**

The core scenario and the fictional dataset are genuinely well constructed. The problem is not the workflow hypothesis, which remains reasonable, it's that the test as written cannot produce a trustworthy answer to the question it claims to answer, in either direction. Several structural issues would bias the result toward a false positive for Ikhaya, and one design gap (no "competent plus one good instruction" condition) means the test can't actually isolate what the six-stage method adds over the cheapest possible fix. These aren't scoring tweaks. They require rebuilding the comparison conditions and decoupling the Checks/rubric from the trap list before this test can be trusted either to validate or kill the workflow.

---

## What's genuinely strong, stated first

- The Northstar scenario is realistic and well-observed. The pulled-forward order, the partially-quantified freight increase, and the overdue-versus-bad-debt distinction are exactly the kind of judgement traps a real finance manager encounters. Whoever wrote this understands management accounting.
- Treating source figures as pre-validated and keeping the test scoped to narrative/judgement rather than arithmetic is the right boundary, and matches the proposition's own stated limits.
- The "critical failures" list (inventing a figure, calling overdue debt bad debt, etc.) is a sound instinct: some failures should matter regardless of total score.

None of that is in question. What follows is why the test still can't be trusted as designed.

---

## Finding 1 — Test A is not a fair proxy for "normal competent use," and this is the single biggest problem

The brief asks whether the Ikhaya method beats "normal competent AI use." Test A's prompt is reasonably well-written, but it contains no instruction at all about hedging, uncertainty, or not stating unconfirmed causes as fact. That specific piece of advice, ask the AI to separate what's known from what's inferred, don't let it invent causation, is not obscure. It's exactly the kind of technique that shows up repeatedly and prominently in the market research this project is built on (`research/ai-workday-system/market-research.md`, section 2.4 and section 4.2): free official guides from Anthropic and Microsoft, and an entire cottage industry of "why your ChatGPT answers are bad" content, already teach "add constraints, ask it not to guess" as baseline good practice in 2026.

A genuinely competent user, the exact customer segment the proposition targets (someone who's "already tried ChatGPT/Claude/Copilot, seen useful results"), is a plausible candidate to already know to add one sentence like: *"Only state something as a cause if the evidence given supports it; flag anything uncertain as a question rather than asserting it."*

Test A as written omits exactly that sentence. If adding it closes most of the gap to Test B, the six-stage method's actual marginal value is far smaller than a two-condition test (nothing vs. full method) can show. **The test currently cannot tell the difference between "our method works" and "a single good instruction works, and we've simply withheld that instruction from the control."**

## Finding 2 — The Checks in Test B are largely a hand-written answer key for this specific dataset, not a generic, reusable procedure

Compare the "Embedded traps" list to the "Checks" list. They line up almost one-to-one: check 3 exists because of the £145k order trap, check 6 exists because of the freight/payroll partial-explanation traps, check 7 exists because of the receivables trap. The Checks weren't derived from general management-accounting verification principles and then found to happen to catch these traps, they were built by someone who already knew the traps, specifically to catch them.

This matters because the product's actual promise, stated plainly in the proposition, is a **repeatable** method: a customer builds their own Checks for their own company's numbers, without a test designer pre-loading the answer key. This test demonstrates that a check list can catch traps when the person writing the check list already knows what the traps are. It does not demonstrate that a finance manager, taught the general method, could construct equally effective checks for a July variance pack they haven't seen the traps in advance for. That's a materially different, and much harder, claim, and it's the one that actually needs testing.

## Finding 3 — The scoring rubric is not independent of the Checks, so a high Test B score is close to circular

Eight of the twelve rubric dimensions (numerical fidelity, evidence discipline, causal restraint, timing recognition, materiality, fact vs inference, partial-explanation handling, cash/risk language) map directly onto the same trap list that generated the Checks in Finding 2. A Checks process explicitly instructed to catch these eight things, scored against a rubric explicitly rewarding catching these eight things, will score well almost by construction. This isn't independent measurement, it's the same specification checked against itself twice.

## Finding 4 — The rubric structurally rewards over-hedging, and nothing in the test catches it

Every rubric dimension pushes toward caution, restraint, flagging, and not-stating. Only one dimension ("Executive usefulness") and a softly worded "verification burden" dimension push the other way. A method that responded to every ambiguous number with "this requires further investigation" would score close to maximum on ten of twelve dimensions while barely being penalised for being useless to an MD who needs an actual read on the month. The scenario includes no case where the correct behaviour is to state something plainly and *not* hedge (for example, the genuine, uncomplicated revenue beat, even accounting for the pulled-forward order, is real and doesn't need heavy qualification). Without a trap that punishes excessive caution as its own failure mode, the test is one-sided: it can only detect "too bold," never "too useless to bother reading."

## Finding 5 — Verification burden and time saved, the actual crux of the hypothesis, have no defined measurement method

The proposition's own success criterion is explicit: does the method work "without creating so much verification work that the benefit disappears." The test's "Verification burden" rubric line is a single 0–2 subjective score, and "Time/effort comparison" in the results template is a blank field with no instructions for how it should actually be measured, no defined proxy (word count checked, number of claims requiring independent traceback, an actual timed read-through by a real finance professional), nothing. This is the part of the hypothesis most likely to kill the product if it's true, and it's the part the test is least equipped to actually measure.

## Finding 6 — Single-shot, single-model, no repetition, no blinding

The test as written runs each condition once, in one model, and the same person presumably scores both. Language models are not perfectly deterministic; a single Test B run could look strong or weak partly by chance rather than because the method is sound or unsound, and there's no plan to run multiple trials, multiple models, or have someone blind to which output is which do the scoring. Given how much is riding on this one test (a go/no-go on a paid product), a single unrepeated run in one tool is thin evidence in either direction.

## Finding 7 — Missing failure modes worth adding

- **Sign/direction errors.** A common, dangerous failure class in AI-assisted finance commentary: misreporting a variance as favourable when it's adverse, or vice versa. Not tested here at all, and arguably more dangerous to an MD than a hedged causal claim.
- **Confidentiality/data-handling.** The proposition itself flags that the "Messy Evidence" workflow requires attention to employer policy and approved tools. This test involves feeding a fictional but realistic-looking set of company financials into an AI tool; a real version of this test should at least note whether either condition prompts appropriate caution about what's being pasted where, since that's part of the product's own stated boundaries elsewhere.
- **Degraded-fidelity replication.** No version of the test checks what happens when a user applies an approximate, personally-adapted version of the method rather than the test designer's exact wording, which is the realistic customer condition, not the ideal one.

## Answering the specific questions asked

**Is Test A unrealistically weak?** Yes, see Finding 1. It represents no-guidance-at-all rather than the best plausible "normal competent" alternative.

**Is Test B unfairly over-engineered to win?** Yes, see Findings 2 and 3. The Checks are dataset-specific, not generic, and the rubric shares the same source.

**Are the embedded traps realistic?** Yes, this part is genuinely good and shouldn't be changed.

**Does the rubric measure genuine customer value?** Partially. It measures accuracy/caution well and usefulness poorly, see Finding 4.

**Are important failure modes missing?** Yes, see Finding 7.

**Does the test adequately measure verification burden and time saved?** No, see Finding 5, this is currently undefined.

**Could this produce a false positive for Ikhaya?** Very likely, as designed, for the combined reasons in Findings 1–4.

**Could this produce a false negative?** Less likely given the above bias, but possible for a narrower reason: a single unrepeated run asking the model to execute eight sequential checks correctly could fail on execution brittleness in one session without that reflecting on whether the underlying method is sound, see Finding 6.

**Could a modern ChatGPT/Claude/Copilot user get essentially the same result with a normal good prompt?** This is the test's most important open question, and as designed, it cannot answer it, because no condition currently tests "good prompt, one extra sentence" as a middle ground between nothing and the full method.

**Is this genuinely something a finance professional might pay to learn as a repeatable method?** Not something this test can currently speak to, since it validates a test-designer-curated implementation on one dataset, not a customer's ability to build their own version, see Finding 2.

---

## What should change before re-running

1. **Add a third condition, Test A2: "competent plus one instruction."** Same prompt as Test A, with a single added sentence of the kind already common in free public guidance (do not state unconfirmed causes as fact; flag uncertainty). This is the comparison that actually tests the method's marginal value.
2. **Rewrite the Test B Checks as generic principles, not scenario-specific triggers.** They should read like a checklist a finance manager could apply to a July pack, an August pack, or a different company entirely, without needing to already know this dataset's traps. If the generic version still catches the Northstar traps, that's real evidence. If it needs Northstar-specific wording to work, that's evidence against the "repeatable method" claim.
3. **Decouple scoring from design.** Either have someone who did not write the Checks build the rubric independently, or build the rubric from general finance-commentary quality standards rather than from this test's own trap list.
4. **Add a usefulness/over-hedging counterweight.** At minimum, one rubric dimension or one critical-failure condition that penalises unnecessary hedging on something the evidence actually does support plainly (the genuine revenue beat is a good candidate).
5. **Define the time/verification-burden measurement concretely** before running the test, not after. At minimum: count of independently-traceable claims requiring manual verification, or an actual timed read-through.
6. **Run each condition at least 2–3 times, ideally across more than one model (Claude and ChatGPT and Copilot, given the product is meant to work across all three), before drawing a conclusion from a single run.**

## What should not change

The scenario, the underlying dataset, and the embedded traps are well built and should be kept largely as they are. The six-stage framework itself is not being challenged here, only whether this particular test can fairly judge it.
