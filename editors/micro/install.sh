#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/micro/colorschemes"
mkdir -p "$DEST"

for f in themes/*.json; do
    name="xscriptor-$(basename "$f")"
    cp "$f" "$DEST/$name"
    echo "  \u2713 $name"
done

echo "Done! Micro themes installed to $DEST"
