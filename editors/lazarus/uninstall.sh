#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.lazarus/editors"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.xml"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.xml"
    fi
done

echo "Done."
