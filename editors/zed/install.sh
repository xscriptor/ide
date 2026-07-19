#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/zed/themes"
mkdir -p "$DEST"
SRC="$(dirname "$0")/themes"
cp "$SRC"/"Xscriptor"*.json "$DEST"
echo "Installed Xscriptor themes to $DEST"
