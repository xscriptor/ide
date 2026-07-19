#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/lite-xl/colors"
mkdir -p "$DEST"

for f in themes/*.lua; do
    cp "$f" "$DEST/$(basename "$f")"
    echo "  \u2713 $(basename "$f")"
done

echo "Done! Lite XL themes installed to $DEST"
