#!/bin/bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
THEMES_DIR="$DIR/themes"

case "$(uname -s)" in
  Darwin)
    NB_DIR="$HOME/Library/Application Support/NetBeans"
    ;;
  Linux)
    NB_DIR="$HOME/.netbeans"
    ;;
  *)
    echo "Unsupported OS: $(uname -s)" >&2
    exit 1
    ;;
esac

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

if [ "$UNINSTALL" = true ]; then
  echo "Uninstalling Xscriptor themes from $NB_DIR"
  for f in "$THEMES_DIR"/*.xml; do
    name="$(basename "$f")"
    find "$NB_DIR" -name "$name" -exec rm -v {} \; 2>/dev/null || true
  done
  echo "Done."
  exit 0
fi

echo "Installing Xscriptor NetBeans themes"
echo "  Copying XML theme files. Import via Tools > Options > Font & Colors > Import."
echo ""

count=0
for f in "$THEMES_DIR"/*.xml; do
  name="$(basename "$f")"
  theme_name="${name%.xml}"
  if [ -n "$FILTER" ] && [ "$theme_name" != "$FILTER" ]; then
    continue
  fi
  echo "  $name"
  count=$((count + 1))
done

if [ "$count" -eq 0 ]; then
  echo "No themes found to install."
  exit 1
fi

echo ""
echo "To import, open NetBeans: Tools > Options > Font & Colors > Import"
echo "Select the desired XML file and apply."
