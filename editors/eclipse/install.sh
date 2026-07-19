#!/bin/bash
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
THEMES_DIR="$DIR/themes"

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

ECLIPSE_DIRS=(
  "$HOME/.eclipse"
  "$HOME/eclipse"
  "$HOME/Applications/Eclipse"
)

if [ "$UNINSTALL" = true ]; then
  echo "Uninstalling Xscriptor Eclipse themes from $THEMES_DIR"
  echo "  Eclipse themes are .epf files imported manually via File > Import > Preferences."
  echo "  To remove, re-import your previous preferences file."
  exit 0
fi

echo "Installing Xscriptor Eclipse themes"
echo "  Eclipse themes are .epf files. Import manually via:"
echo "    File > Import > Preferences > Browse > select .epf file"
echo ""
echo "Available themes in $THEMES_DIR:"
for f in "$THEMES_DIR"/*.epf; do
  name="$(basename "$f" .epf)"
  if [ -z "$FILTER" ] || [ "$name" = "$FILTER" ]; then
    echo "  - $name"
  fi
done
echo ""
echo "To import: open Eclipse, go to File > Import > Preferences, browse to the .epf file."
