# Test 01 v2 — Claude Trial Evaluation

**Evaluator:** Claude (Anthropic), same instance that generated the raw outputs
**Date:** 20 August 2026
**Raw outputs evaluated:** `results/test-01-claude-raw.md`

---

## Critical limitation, stated before any numbers

This entire round was generated and scored by the same Claude instance, working in one continuous context, who also wrote the original adversarial review and contributed to the redesign this test is built on. That instance knew the hidden evaluation traps while drafting every output, even though it deliberately tried not to write toward or away from them. This is a real, significant source of possible bias, not a formality. Two specific risks are worth naming directly:

1. **The Condition A2 outputs in this round may be unrealistically strong**, because they were written by an instance that already understood, in detail, exactly which inferential leap the test wanted A2 to avoid (the £145k order being a timing effect rather than confirmed growth). A real, independently-run Claude session given only the one-sentence A2 instruction ("only state a cause when the information supports it") might not spontaneously extend that same rigour to a framing/classification issue like the order timing, since that isn't literally a stated "cause," it's closer to a categorisation the A2 instruction doesn't explicitly ask for. If that's right, this round's A2 outputs look more like a hybrid of A2's actual instruction and B's explicit "timing versus underlying economics" check, which would make A2 appear artificially close to B.
2. **Scoring was done by the same party whose review shaped the redesign**, which the test specification itself flags as a problem worth avoiding ("the person who designed the Ikhaya prompt should not be the sole judge of whether Ikhaya won"). The reverse concern applies here too: since I also wrote the critical review that pushed for a harder A2 control, I have some motivation to make A2 look strong, to avoid my own earlier critique looking overstated. I don't believe I did this deliberately, but I can't rule it out, and neither should the reader.

**Conclusion up front: this round should be treated as a rough internal signal, not evidence sufficient to decide the product's fate.** The test specification's own blinding and replication requirements exist precisely to guard against the two risks above, and this round doesn't meet them. Genuine independent sessions (ideally run by someone other than the method's author, and scored blind) are needed before this question is actually settled.

With that stated plainly, here is what this round found.

---

## Scores

0 = material weakness, 1 = acceptable/mixed, 2 = strong. Maximum 20 per output.

| Dimension | A1 | A2(run) | A3 | A2-1 | A2-2 | A2-3 | B1 | B2 | B3 |
|---|---|---|---|---|---|---|---|---|---|
| Accuracy | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Analytical validity | 0 | 1 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| Explanatory calibration | 0 | 1 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| Materiality/prioritisation | 1 | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Commercial usefulness | 1 | 1 | 1 | 2 | 2 | 2 | 1 | 2 | 2 |
| Clarity and brevity | 2 | 2 | 2 | 1 | 1 | 2 | 1 | 2 | 2 |
| Risk judgement | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| Action quality | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Traceability | 1 | 1 | 1 | 2 | 2 | 2 | 2 | 2 | 2 |
| Human verification effort | 0 | 1 | 0 | 2 | 2 | 2 | 2 | 2 | 2 |
| **Total /20** | **9** | **14** | **10** | **19** | **19** | **20** | **18** | **20** | **20** |

### Condition averages

| Condition | Average /20 | Range |
|---|---|---|
| A (ordinary competent use) | **11.0** | 9–14 |
| A2 (+ single uncertainty instruction) | **19.3** | 19–20 |
| B (Ikhaya generic method) | **19.3** | 18–20 |

**A and A2 differ by 8.3 points on average. A2 and B differ by 0.0 points on average in this round.**

---

## Critical failures

| Run | Critical failure(s) |
|---|---|
| A1 | Unsupported causal claim presented as fact ("broader margin softness" with no supporting evidence); timing/phasing item (the £145k pulled-forward order) not raised at all and revenue beat described as "encouraging top-line growth", materially misrepresenting a timing effect as underlying performance |
| A2(run, second A run) | No hard critical failure, but borderline: freight and payroll causes stated with more confidence than the source data supports |
| A3 | Timing/phasing item materially misrepresented as underlying performance ("showing good underlying demand" stated directly from the revenue beat without acknowledging the pulled-forward order) |
| A2-1, A2-2, A2-3 | None identified |
| B1, B2, B3 | None identified |

**Condition A produced 2 clear critical failures and 1 borderline case across 3 runs. Neither A2 nor B produced any critical failures in this round.**

---

## Verification-burden observations

All figures below are **estimates**, not measured, timed observations, per the test's own instruction that the first genuine human-timing round should come from actual target users, not the same party running the test.

| Condition | Material claims count (avg, est.) | Unsupported/problem claims (avg, est.) | Traceback friction | Correction effort (est. minutes) | Discard/rebuild? |
|---|---|---|---|---|---|
| A | ~9 | ~2.3 | Medium–High (causal claims not tied to which fact supports them) | 12–18 | Yes, for A1 and A3 specifically; A2(run) closer to repairable |
| A2 | ~10 | ~0.3 | Low (each claim is explicitly linked to a named gap or fact) | 3–6 | No |
| B | ~10 | ~0.3 | Low (explicit structure separates confirmed points from open questions) | 3–6 | No |

**On this measure, A2 and B again look very similar**, both substantially reduce estimated correction effort versus A, and neither shows a meaningful edge over the other. This is the same pattern as the quality scores, and carries the same caveat: these are estimates from the same self-interested evaluator, not timed data from an actual finance professional.

---

## Run-to-run variation

**Condition A varied the most** (range 9–14/20). A2(run), the second A run, happened to acknowledge the pulled-forward order in passing, which meaningfully improved its score versus A1 and A3, neither of which raised it at all. This suggests ordinary, unguided use is inconsistent from session to session on whether it catches the most important trap in this scenario, which is itself a relevant finding: an ungoverned process's quality is not just lower on average, it's less predictable.

**Condition A2 and B were both consistent** (A2: 19–20, B: 18–20), each run reliably avoided the hidden traps once given either the single instruction or the full method. B1 was marked down slightly for an internal drafting inconsistency (a clumsy, partially self-correcting sentence, left unaltered per instruction) rather than any conceptual failure, which is a reminder that B's extra structure doesn't guarantee flawless execution either.

---

## A vs A2 vs B, and the marginal question the test was built to answer

**What does A2 add over A?** A large amount, in this round: it is the difference between two critical failures in three runs and zero, and between double-digit and near-maximum scores. This part of the result is credible even accounting for the self-scoring limitation, because Condition A wasn't given any special treatment either way, it was simply asked the plain question, and its failure modes (stating the revenue beat as confirmed strength, treating freight/payroll causes as fully established) match exactly the pattern the underlying research and the original adversarial review predicted.

**What does B add over A2 that this round can actually demonstrate?** Almost nothing measurable. B's average score matches A2's average score exactly. B did not produce fewer critical failures than A2 (both had none in this round). B's estimated verification burden was not meaningfully lower than A2's.

**Is that a fair conclusion, or an artefact of how this round was run?** Most likely the latter, at least partly, for the reason stated in the limitation section: the same author who knows B's explicit "timing versus underlying economics" check also wrote the A2 outputs, and appears to have carried that same discipline into A2 even though A2's actual instruction doesn't explicitly demand it. **This is the single most important thing for a genuinely independent replication to test**: whether an ordinary user, given only the one-sentence A2 instruction with no knowledge of the fuller method, would reliably catch a purely classificatory issue (order timing vs. genuine growth) that isn't literally about "stating a cause." My honest expectation, setting aside what I actually produced in this self-run round, is that a real independent A2 session is somewhat less likely than these outputs to catch the timing framing specifically, because the A2 instruction is worded around causation, not classification. If that expectation is right, a fair independent test would likely show a real, if modest, B advantage concentrated specifically on the timing-classification point and on the "usefulness versus caution" balance, both of which B's Checks name explicitly and A2's single instruction does not.

**Where does the apparent advantage, such as it is, actually come from?** Not from better underlying reasoning capability (Condition A2 shows Claude is clearly capable of the same calibrated reasoning B produces, once prompted). Not from length or structure for its own sake, B's extra formatting (executive summary, numbered priority points, explicit human-decision statement) is presentation, not information content, and A2's plainer format didn't lose points on the rubric for lacking that formatting. Not from excessive caution, neither A2 nor B in this round showed the "buried in caveats" failure mode; if anything A2's phrasing was occasionally slightly more repetitive than B's, without materially hurting clarity. The most plausible source of any real, replicable B advantage is narrower and more specific than the full six-stage apparatus: **the explicit instruction to check for timing/classification effects, and the explicit instruction to balance caution against usefululness**, both of which could very plausibly be added to a "cheapest plausible free improvement" as one or two more sentences, well short of a full paid method.

---

## Direct answers to the questions asked

**What does B achieve that A2 does not?** In this self-administered round: essentially nothing measurable. The honest, more useful answer is that B's *design* names two specific checks (timing/classification, and caution-versus-usefulness) that a bare-minimum A2 instruction doesn't explicitly cover, and that's the real candidate for where a genuine, independently-tested advantage would come from, not the six-stage structure as a whole.

**If the answer is weak, say so.** It is weak, as measured in this round. State it plainly: this round did not find B outperforming A2 in any dimension that would survive independent replication with confidence.

**Does any apparent advantage come from better reasoning, structure, more words, excessive caution, or instructions a competent user could reproduce for free?** Where any advantage exists in this round, it traces to instructions, not underlying reasoning capability, and those instructions (checking for timing effects, balancing caution against usefulness) are short, specific, and easily reproducible for free by adding a sentence or two to A2, not by buying a six-stage paid method. That is the most important, and most uncomfortable, finding of this round for the product's commercial case.

---

## Provisional verdict: **MODIFY**

Not KEEP: this round does not show B producing a repeatable, independently-credible advantage over A2, which is the test's own bar for KEEP ("B must show a repeatable advantage over A2 ... the advantage must survive multiple runs and not depend on Northstar-specific wording"). The near-identical scores here most likely reflect contamination from self-authorship rather than a genuine null result, but that itself means KEEP cannot be supported yet.

Not DROP: Condition A's clear, repeated failure relative to both A2 and B confirms the underlying problem (ungoverned AI use on financial commentary produces real, critical errors) is genuine and not imagined. And the specific mechanism that might separate B from A2, explicit timing/classification checking and caution/usefulness balancing, is a plausible, specific, testable hypothesis, not yet ruled out.

**MODIFY**, specifically: before any further product decision, run genuinely independent sessions (not self-authored by the method's designer), ideally across both Claude and ChatGPT as the test specification requires, with blind scoring by someone who did not write either the Checks or the A2 instruction. If that independent round still shows A2 matching B, the six-stage method should be simplified down to whatever the two or three specific checks are that actually carry the demonstrated advantage, rather than sold as a full framework. If it shows a real, replicated B advantage concentrated on timing/classification and caution-balance, the method can proceed, but should foreground those two specific checks as the actual value proposition rather than the six-stage structure in general.

---

## What this teaches us about the product, provisionally

The most commercially important finding from this round isn't a score, it's a methodological one: **a single sentence of good instruction gets a competent AI user most of the way to what the full Ikhaya method produces**, at least for this scenario, as tested here. If that holds up under genuinely independent, blind replication, Ikhaya's defensible product is much narrower than "a six-stage method for AI-assisted finance work." It may be closer to: a small number of specific, well-chosen checks per job type, taught briefly, rather than a full framework requiring guided workflow-building. That would still be worth something, arguably it's a leaner, more honestly-scoped product than the current proposition describes, but it's a different, smaller product than the one currently being built toward, and the team should decide deliberately whether to narrow toward that before investing further in the six-stage structure as the core deliverable.
