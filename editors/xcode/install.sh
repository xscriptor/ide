#!/bin/bash
#
# install.sh -- Install Xcode themes from themes/ into Xcode's FontAndColorThemes directory.
#
# Usage:
#   ./install.sh                            # install all themes (local)
#   ./install.sh Praha                      # install a single theme (local)
#   curl ... | REPO="xscriptor/xcode" bash        # remote install
#   curl ... | REPO="xscriptor/xcode" bash -s -- -u  # remote uninstall
#   ./install.sh -u                         # uninstall all themes
#   ./install.sh -h                         # show help
#
# Remote usage (requires REPO environment variable):
#   REPO="xscriptor/xcode" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh)
#   REPO="xscriptor/xcode" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh) -s Praha
#

set -euo pipefail

XDEST="$HOME/Library/Developer/Xcode/UserData/FontAndColorThemes"

THEMES=(X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota)

usage() {
  echo "Usage: $(basename "$0") [theme-name | -u | -h]"
  echo ""
  echo "  theme-name    Install a single theme (e.g. Praha)"
  echo "  -u, --uninstall  Remove installed themes from Xcode"
  echo "  -h, --help       Show this help"
  echo ""
  echo "Remote install (set REPO environment variable):"
  echo "  REPO=\"xscriptor/xcode\" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh)"
  exit 0
}

is_local() {
  local dir
  dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" 2>/dev/null && pwd)" || dir="."
  [ -d "$dir/themes" ]
}

download_theme() {
  local name="$1" outdir="$2"
  local url="https://raw.githubusercontent.com/$REPO/main/themes/$name.xccolortheme"
  if command -v curl &>/dev/null; then
    curl -fsSL "$url" -o "$outdir/$name.xccolortheme"
  elif command -v wget &>/dev/null; then
    wget -q "$url" -O "$outdir/$name.xccolortheme"
  else
    echo "Error: curl or wget required for remote install." >&2
    exit 1
  fi
}

if [ "${1:-}" = "-u" ] || [ "${1:-}" = "--uninstall" ]; then
  echo "Uninstalling themes from $XDEST ..."
  for name in "${THEMES[@]}"; do
    target="$XDEST/$name.xccolortheme"
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

if is_local; then
  MODE="local"
  SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/themes" && pwd)"
else
  if [ -z "${REPO:-}" ]; then
    echo "Error: REPO environment variable is required for remote install." >&2
    echo "" >&2
    echo "  REPO=\"xscriptor/xcode\" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh)" >&2
    exit 1
  fi
  MODE="remote"
fi

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
  case "$MODE" in
    local)
      srcfile="$SRC/$name.xccolortheme"
      if [ ! -f "$srcfile" ]; then
        echo "Error: $srcfile not found." >&2
        exit 1
      fi
      cp -v "$srcfile" "$XDEST/"
      ;;
    remote)
      echo "Downloading $name ..."
      download_theme "$name" "$XDEST"
      ;;
  esac
else
  case "$MODE" in
    local)
      cp -v "$SRC"/*.xccolortheme "$XDEST/"
      ;;
    remote)
      echo "Downloading themes from $REPO ..."
      for name in "${THEMES[@]}"; do
        echo "  $name"
        download_theme "$name" "$XDEST"
      done
      ;;
  esac
fi

echo ""
echo "Installation complete. Restart Xcode and select the theme from:"
echo "  Xcode > Preferences > Themes"
