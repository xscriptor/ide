#!/bin/bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
THEMES_DIR="$DIR/themes"

case "$(uname -s)" in
  Darwin)
    ST_DIR="$HOME/Library/Application Support/Sublime Text"
    ;;
  Linux)
    ST_DIR="$HOME/.config/sublime-text"
    ;;
  *)
    echo "Unsupported OS: $(uname -s)" >&2
    exit 1
    ;;
esac

USER_DIR="$ST_DIR/Packages/User"

usage() {
  echo "Usage: $0 [-u] [theme_name]"
  echo "  -u           Uninstall themes"
  echo "  theme_name   Install only the specified theme (e.g. Praha)"
  exit 1
}

UNINSTALL=false
FILTER=""
if [ $# -gt 0 ]; then
  case "$1" in
    -u) UNINSTALL=true ;;
    -h|--help) usage ;;
    *) FILTER="$1" ;;
  esac
fi

mkdir -p "$USER_DIR"

if [ "$UNINSTALL" = true ]; then
  echo "Uninstalling Xscriptor themes from $USER_DIR"
  for f in "$THEMES_DIR"/*.sublime-color-scheme; do
    name="$(basename "$f")"
    target="$USER_DIR/$name"
    if [ -f "$target" ]; then
      rm "$target"
      echo "  removed $name"
    fi
  done
  echo "Done."
  exit 0
fi

echo "Installing Xscriptor themes to $USER_DIR"
count=0
for f in "$THEMES_DIR"/*.sublime-color-scheme; do
  name="$(basename "$f")"
  if [ -n "$FILTER" ] && [[ "$name" != "$FILTER.sublime-color-scheme" ]]; then
    continue
  fi
  cp "$f" "$USER_DIR/$name"
  echo "  installed $name"
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "No themes found to install."
  if [ -n "$FILTER" ]; then
    echo "Theme '$FILTER' not found in $THEMES_DIR"
  fi
  exit 1
fi

echo "Done. $count theme(s) installed. Restart Sublime Text and select from Preferences > Color Scheme."
