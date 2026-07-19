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

if [ "$UNINSTALL" = true ]; then
  echo "Uninstalling Xscriptor Visual Studio themes"
  echo "  .vssettings files are imported manually. To remove, re-import your previous settings."
  exit 0
fi

echo "Installing Xscriptor Visual Studio themes"
echo "  .vssettings files must be imported manually via:"
echo "    Tools > Import/Export Settings > Import > Browse"
echo ""
echo "Available themes in $THEMES_DIR:"
for f in "$THEMES_DIR"/*.vssettings; do
  name="$(basename "$f" .vssettings)"
  if [ -z "$FILTER" ] || [ "$name" = "$FILTER" ]; then
    echo "  - $name"
  fi
done
echo ""
echo "To import, open Visual Studio: Tools > Import/Export Settings > Import"
echo "Select the desired .vssettings file and follow the prompts."
