#!/usr/bin/env bash
set -euo pipefail

for dest in \
    "/usr/lib/python3/dist-packages/cudatext/app/data/color" \
    "/usr/share/cudatext/data/color" \
    "$HOME/.config/cudatext/data/color"; do
    if [ -d "$dest" ]; then
        for f in themes/*.json; do
            rm -f "$dest/$(basename "$f")"
        done
    fi
done

echo "Done. Xscriptor CudaText themes removed."
