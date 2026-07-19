#!/usr/bin/env bash
set -euo pipefail

DEST="$HOME/.codelite/themes"
mkdir -p "$DEST"

for f in themes/*.json; do
    cp "$f" "$DEST/$(basename "$f")"
    echo "  \u2713 $(basename "$f")"
done

echo "Done! CodeLite themes installed to $DEST"
