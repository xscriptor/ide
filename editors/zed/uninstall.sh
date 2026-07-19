#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/zed/themes"
rm -f "$DEST"/"Xscriptor"*.json
echo "Removed Xscriptor themes from $DEST"
