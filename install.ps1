# The Stoic — installer for Claude Code (Windows).
#
# Copies SKILL.md into ~/.claude/skills/stoic/ so Claude Code picks it up as
# a real skill. Safe to re-run — overwrites its own prior install only.

$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$SourceFile = Join-Path $ScriptDir "SKILL.md"
$DestDir = Join-Path $env:USERPROFILE ".claude\skills\stoic"

if (-not (Test-Path $SourceFile)) {
    Write-Error "SKILL.md not found next to this script. Run install.ps1 from inside the cloned repo."
    exit 1
}

if (-not (Test-Path $DestDir)) {
    New-Item -ItemType Directory -Force -Path $DestDir | Out-Null
}

Copy-Item -Path $SourceFile -Destination (Join-Path $DestDir "SKILL.md") -Force

Write-Host "Installed: $DestDir\SKILL.md"
Write-Host "Restart Claude Code (or reload skills, if your version supports it) to pick it up."
Write-Host 'Try it: say "stoic mode" in a session, or "automode on" to let it decide on its own.'
