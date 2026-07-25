# Benchmark: output-token reduction by level

**Methodology, honestly stated:** this is an *approximate* measurement, not a real Claude API
count. It runs 5 matched baseline/lite/full/ultra response pairs (same content, written by hand
to represent realistic Claude Code replies — a debugging explanation, a regex explanation, a
step-preamble-protected action, a concept explanation, and a short status confirmation) through
`tiktoken`'s `cl100k_base` encoding, which is **not** Claude's actual tokenizer. Treat the
percentages below as directionally correct, not exact — a real API-based benchmark (using
Anthropic's token-counting endpoint against live responses) is the natural next step and would
replace this file's numbers, not just add to them.

Reproduce: `python benchmarks/bench.py` (requires `pip install tiktoken`).

## Results (2026-07-25)

| Case | Baseline | lite | full | ultra | lite Δ | full Δ | ultra Δ |
|------|---------:|-----:|-----:|------:|-------:|-------:|--------:|
| debugging-explanation | 152 | 78 | 55 | 24 | 48.7% | 63.8% | 84.2% |
| regex-explanation | 155 | 84 | 62 | 24 | 45.8% | 60.0% | 84.5% |
| step-preamble-action | 135 | 52 | 52 | 52 | 61.5% | 61.5% | 61.5% |
| concept-explanation | 169 | 74 | 48 | 19 | 56.2% | 71.6% | 88.8% |
| status-confirmation | 54 | 14 | 12 | 5 | 74.1% | 77.8% | 90.7% |
| **Total** | **665** | **302** | **229** | **124** | **54.6%** | **65.6%** | **81.4%** |

## Reading this honestly

- **`step-preamble-action` doesn't improve past lite** — by design. The step-preamble exception
  (see `SKILL.md` → "Stay-explained exceptions") forces the same full plain-language sentence at
  every level for any state-changing action; only the *closing* line compresses further at
  higher levels. A skill that compressed this case further wouldn't be doing its job.
- **Short, already-terse answers (`status-confirmation`) show the highest percentage reduction**
  — makes sense, since the baseline itself is mostly filler ("I'm happy to report...") around a
  small factual core. Longer analytical answers save less *percentage-wise* because more of their
  length is genuinely load-bearing content, not filler.
- These 5 cases are illustrative, not a statistically representative sample of real usage. A
  real benchmark would draw from actual transcripts, not hand-written pairs — flagged in
  `CONTRIBUTING.md` as a real, useful contribution if someone wants to build it properly.
