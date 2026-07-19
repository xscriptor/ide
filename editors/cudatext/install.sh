#!/usr/bin/env bash
set -euo pipefail

# Detect common CudaText color directory
if [ -d "/usr/lib/python3/dist-packages/cudatext/app/data/color" ]; then
    DEST="/usr/lib/python3/dist-packages/cudatext/app/data/color"
elif [ -d "/usr/share/cudatext/data/color" ]; then
    DEST="/usr/share/cudatext/data/color"
elif [ -d "$HOME/.config/cudatext/data/color" ]; then
    DEST="$HOME/.config/cudatext/data/color"
else
    DEST="$HOME/.config/cudatext/data/color"
fi

mkdir -p "$DEST"

for f in themes/*.json; do
    cp "$f" "$DEST/$(basename "$f")"
    echo "  \u2713 $(basename "$f")"
done

echo "Done! CudaText themes installed to $DEST"
