# The Stoic

**A Claude Code skill that cuts output-token filler — and never cuts the "why."**

For anyone running Claude Code who wants shorter replies without losing the plain-language
explanation of what's about to happen before a command or file edit runs. Code, commands,
errors, and file paths stay byte-exact at every level.

Quiet and precise instead of loud and clipped — a deliberate upgrade on the "caveman" style of
compression skill, not a clone of one.

## Why this exists

Several existing token-compression skills for coding agents do a good job of cutting the filler
around an answer — greetings, restating what a tool call already showed, offers to do more. What
none of them do well is protect the *ordinary* step-by-step narration a careful user actually
wants kept — the "here's what I'm about to run and why" sentence before a command or file edit.
Their safety mechanisms typically only suspend compression for emergencies (security warnings,
destructive actions), not for routine action explanations.

The Stoic adds a fifth, always-on exception category — **step preambles** — specifically for
this. One full plain-language sentence before any state-changing action, kept short but never
compressed to a fragment and never skipped, regardless of active compression level. See
`SKILL.md` → "Stay-explained exceptions" for the full mechanism.

## Levels

Three levels, chosen by how much sentence structure gets dropped — never by touching technical
content:

- **lite** (default) — cuts filler, hedging, and pleasantries; keeps full sentences and articles.
- **full** — also drops articles, uses fragments, cuts tool-call narration beyond what's asked.
- **ultra** — also collapses multi-clause sentences into one fact per line, drops connective
  words when order alone still carries the causal link.

Measured (approximate, not a real Claude API count — see `benchmarks/results.md` for full
methodology and caveats): **54.6% / 65.6% / 81.4%** output-token reduction at lite/full/ultra
across 5 representative cases.

## AutoMode

Explicit-invocation is the default. An opt-in **AutoMode** (`automode on` / `automode off`) lets
the skill decide on its own, per reply, whether to go stoic and which level to use — with a
separate `conservative` / `balanced` / `aggressive` sensitivity dial controlling how readily it
triggers. AutoMode never touches the stay-explained exceptions: step preambles and the other
protected content stay absolute no matter how AutoMode is configured. Full mechanism in
`SKILL.md`.

## Install

**Claude Code:**

```
./install.sh      # macOS / Linux
./install.ps1      # Windows PowerShell
```

This copies `SKILL.md` into `~/.claude/skills/stoic/`. Restart Claude Code (or run `/skills
reload` if your version supports it) so the new skill is picked up.

**Other agents:** the skill is a single, self-contained Markdown file with YAML frontmatter — if
your tool supports Claude-Code-style skill files, copying `SKILL.md` into its skills directory
should work. Not independently tested against agents other than Claude Code yet — see Roadmap.

## Roadmap — honestly, what's not built yet

- **Multi-agent support beyond Claude Code.** The skill file itself is plain Markdown and should
  port cleanly, but installers/hooks for Codex, Gemini CLI, Cursor, Windsurf, and others aren't
  built or tested here. Contributions welcome.
- **Usage/stats tracking** (e.g. measuring real token savings per session) — a real idea, not
  built in this repo. Would be its own tool rather than bolted onto this skill, to keep it doing
  one job.
- **A `/stoic` slash-command wrapper** for editors that support custom commands — not built yet,
  the skill currently activates purely on the trigger phrases in its own description.

## Credits

The general idea — a Claude Code skill that trims verbal filler from agent output to save output
tokens — is not new. Two existing projects were real, valuable prior art while designing this
one, and are credited here rather than quietly absorbed:

- [`JuliusBrussee/caveman`](https://github.com/JuliusBrussee/caveman) — the dominant, actively
  maintained implementation of this general idea, with broad multi-agent support and a large
  community. The Stoic is not a fork of it — no code or text from that repo is reused here — but
  its existence, and its documented ~65% output-token reduction, is what proved the underlying
  approach was worth building on.
- [`amanattar/caveman-claude-skill`](https://github.com/amanattar/caveman-claude-skill) — a
  smaller, less-maintained implementation whose graduated intensity-level design (multiple named
  levels, switchable via command) and its "Auto-Clarity" concept (suspending compression for
  certain situations) were genuine design inspiration for this skill's own level system and
  Stay-explained exceptions, reworked and extended from scratch rather than copied.

If you're choosing between them: the original `caveman` has far broader agent support and a much
larger track record. The Stoic trades that breadth for one specific thing neither upstream
project does — protecting ordinary step-by-step explanations, not just emergencies — plus an
opt-in AutoMode with its own sensitivity control.

## License

MIT — see `LICENSE`.
