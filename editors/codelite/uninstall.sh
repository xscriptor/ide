#!/usr/bin/env bash
set -euo pipefail

DEST="$HOME/.codelite/themes"

echo "Removing Xscriptor CodeLite themes..."
for f in themes/*.json; do
    rm -f "$DEST/$(basename "$f")"
done
echo "Done."
