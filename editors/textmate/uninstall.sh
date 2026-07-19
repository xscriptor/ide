#!/bin/bash
#
# uninstall.sh -- Remove TextMate Xscriptor themes.
#
# Usage:
#   ./uninstall.sh                          # remove all themes
#   ./uninstall.sh Praha                    # remove a single theme
#   ./uninstall.sh -h                       # show help
#

set -euo pipefail

XDEST="$HOME/Library/Application Support/TextMate/Themes"

THEMES=(X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota)

usage() {
  echo "Usage: $(basename "$0") [theme-name | -h]"
  echo ""
  echo "  theme-name    Remove a single theme (e.g. Praha)"
  echo "  -h, --help    Show this help"
  exit 0
}

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
fi

if [ ! -d "$XDEST" ]; then
  echo "TextMate themes directory not found: $XDEST" >&2
  exit 1
fi

if [ -n "${1:-}" ]; then
  name="$1"
  found=false
  for t in "${THEMES[@]}"; do
    [ "$t" = "$name" ] && found=true && break
  done
  if ! $found; then
    echo "Error: unknown theme '$name'." >&2
    echo "Available themes: ${THEMES[*]}" >&2
    exit 1
  fi
  target="$XDEST/$name.tmTheme"
  if [ -f "$target" ]; then
    rm -v "$target"
  else
    echo "Theme not installed: $name" >&2
  fi
else
  count=0
  for name in "${THEMES[@]}"; do
    target="$XDEST/$name.tmTheme"
    if [ -f "$target" ]; then
      rm -v "$target"
      count=$((count + 1))
    fi
  done
  if [ "$count" -eq 0 ]; then
    echo "No Xscriptor themes found in $XDEST"
  fi
fi

echo "Done."
