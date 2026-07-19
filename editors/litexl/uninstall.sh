#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/lite-xl/colors"

echo "Removing Xscriptor Lite XL themes..."
for f in themes/*.lua; do
    rm -f "$DEST/$(basename "$f")"
done
echo "Done."
