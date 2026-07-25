# Contributing

Small project, one file that matters (`SKILL.md`) — contributions are welcome, especially in
the areas the README's Roadmap already flags as unbuilt.

## Where help is most useful

1. **Multi-agent installers.** `SKILL.md` is plain Markdown with YAML frontmatter and should
   port to other Claude-Code-style skill loaders (Codex, Gemini CLI, Cursor, Windsurf, etc.),
   but no per-agent install script has been written or tested beyond Claude Code. If you get it
   working on another agent, a PR adding `install-<agent>.sh` plus a short README note is exactly
   the kind of contribution this needs.
2. **Real-world testing.** The compression rules and the stay-explained exceptions (see
   `SKILL.md`) are specified in prose, not code — the actual test is whether they hold up across
   real conversations. If you find a case where a level compresses something it shouldn't, or a
   stay-explained exception doesn't fire when it should, open an issue with the actual exchange
   (redacted if needed) rather than a hypothetical.
3. **Usage/stats tracking.** Flagged in the Roadmap as a real idea, not built — if you want to
   take it on, it should be its own tool rather than bolted onto this skill (see Roadmap for why).

## Proposing a change to SKILL.md

Since there's no code to run, "testing" a change means actually using it in a real Claude Code
session across a few representative prompts (short factual question, multi-step task with a
real action, something that should trigger a stay-explained exception) and including a couple of
before/after examples in the PR description — the same shape as the worked examples already in
the file.

Keep changes scoped to one thing per PR. If a change would meaningfully shift the default
behavior (a level's definition, what counts as a stay-explained exception, AutoMode's default
sensitivity), explain the reasoning in the PR, not just the diff — the existing exceptions all
have a documented "why," not just a "what."

## Reporting an issue

Open a GitHub issue. Include: the trigger phrase or level used, what you expected, what actually
happened, and the model/agent you were running (Claude Code version if relevant).

## License

Contributions are accepted under the same MIT license as the rest of the repo (see `LICENSE`).
