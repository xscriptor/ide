#!/bin/bash
#
# install.sh -- Install TextMate themes from themes/ into TextMate's Themes directory.
#
# Usage:
#   ./install.sh                            # install all themes (local)
#   ./install.sh Praha                      # install a single theme (local)
#   ./install.sh -u                         # uninstall all themes
#   ./install.sh -h                         # show help
#

set -euo pipefail

XDEST="$HOME/Library/Application Support/TextMate/Themes"

THEMES=(X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota)

usage() {
  echo "Usage: $(basename "$0") [theme-name | -u | -h]"
  echo ""
  echo "  theme-name    Install a single theme (e.g. Praha)"
  echo "  -u, --uninstall  Remove installed themes"
  echo "  -h, --help       Show this help"
  exit 0
}

is_local() {
  local dir
  dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || dir="."
  [ -d "$dir/themes" ]
}

if [ "${1:-}" = "-u" ] || [ "${1:-}" = "--uninstall" ]; then
  echo "Uninstalling themes from $XDEST ..."
  for name in "${THEMES[@]}"; do
    target="$XDEST/$name.tmTheme"
    if [ -f "$target" ]; then
      rm -v "$target"
    fi
  done
  echo "Done."
  exit 0
fi

if [ "${1:-}" = "-h" ] || [ "${1:-}" = "--help" ]; then
  usage
fi

if ! is_local; then
  echo "Error: themes/ directory not found. Run from the editors/textmate directory." >&2
  exit 1
fi

SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/themes" && pwd)"
mkdir -p "$XDEST"

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
  srcfile="$SRC/$name.tmTheme"
  if [ ! -f "$srcfile" ]; then
    echo "Error: $srcfile not found." >&2
    exit 1
  fi
  cp -v "$srcfile" "$XDEST/"
else
  cp -v "$SRC"/*.tmTheme "$XDEST/"
fi

echo ""
echo "Installation complete. Restart TextMate and select the theme from:"
echo "  Preferences > Themes"
