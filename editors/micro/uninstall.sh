#!/usr/bin/env bash
set -euo pipefail

DEST="${XDG_CONFIG_HOME:-$HOME/.config}/micro/colorschemes"

echo "Removing Xscriptor Micro themes..."
for f in themes/*.json; do
    name="xscriptor-$(basename "$f")"
    rm -f "$DEST/$name"
done
echo "Done."
