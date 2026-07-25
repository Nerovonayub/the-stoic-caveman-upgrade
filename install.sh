#!/usr/bin/env bash
# The Stoic — installer for Claude Code.
#
# Copies SKILL.md into ~/.claude/skills/stoic/ so Claude Code picks it up as
# a real skill. Safe to re-run — overwrites its own prior install only.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST_DIR="${HOME}/.claude/skills/stoic"

if [ ! -f "${SCRIPT_DIR}/SKILL.md" ]; then
  echo "SKILL.md not found next to this script. Run install.sh from inside the cloned repo." >&2
  exit 1
fi

mkdir -p "${DEST_DIR}"
cp "${SCRIPT_DIR}/SKILL.md" "${DEST_DIR}/SKILL.md"

echo "Installed: ${DEST_DIR}/SKILL.md"
echo "Restart Claude Code (or reload skills, if your version supports it) to pick it up."
echo "Try it: say \"stoic mode\" in a session, or \"automode on\" to let it decide on its own."
