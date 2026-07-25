# Usage

`SKILL.md` is written for the agent, not for a human skimming it — this doc is the plain version:
what to actually type, and what changes when you do.

## Turning it on

Say any of these in a Claude Code session, once installed:

> `stoic mode` · `go stoic` · `cut the filler` · `fewer tokens` · `talk tight` · `compress your
> output` · `/stoic`

It stays on for the rest of the session. Turn it off with `stop stoic`, `normal mode`, or `full
explanations again`.

## Picking a level

Say the level name with the trigger, or on its own once stoic mode is already active:

> `stoic lite` (default) · `stoic full` · `stoic ultra` · or just `lite` / `full` / `ultra`

**What actually changes**, in plain terms:

| Level | You'll notice... |
|-------|-------------------|
| `lite` | Shorter replies — no "happy to help!", no restating what you already saw, no hedging. Still full sentences. |
| `full` | Fragments instead of full sentences. Articles ("the", "a") start disappearing where the meaning survives without them. |
| `ultra` | One fact per line. Terse enough that it reads like notes, not prose. |

Code, commands, error messages, file paths, and numbers are **never** shortened or abbreviated —
at any level. That doesn't change.

## AutoMode — let it decide for you

If you don't want to think about levels or remember to turn it on:

> `automode on`

Now Claude decides per-reply whether to go terse and which level fits, based on how the
conversation is actually going (repetitive tool-heavy exchanges, you saying "just do it," etc.).
Turn it off completely with:

> `automode off`

**Tune how eager it is** (only matters while AutoMode is on):

> `automode conservative` — waits for a strong signal before going terse
> `automode balanced` — the default, engages on one clear signal
> `automode aggressive` — goes terse at the first sign of a repetitive exchange

## What you'll always still get, no matter the level or AutoMode setting

This is the actual point of the skill, not a footnote:

- **Before any real action** (a command, a file edit, a tool call) — one full plain sentence
  explaining what's about to happen and why. Never a fragment, never skipped.
- **Security warnings and anything irreversible** — full explanation, every time.
- **If you say "wait, what?" or seem confused** — that one reply drops back to full plain
  language automatically, no need to say "normal mode" first.
- **If you ask "explain that"** — same, just for the one thing you asked about.

## Quick reference

```
stoic mode / go stoic / /stoic        → turn on (lite)
stoic full / stoic ultra              → turn on at a specific level
stop stoic / normal mode              → turn off
automode on                           → let it decide when + how much
automode conservative|balanced|aggressive → tune how eager AutoMode is
automode off                          → stop deciding on its own
```
