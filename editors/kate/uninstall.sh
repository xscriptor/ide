#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.local/share/kate/color-schemes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.theme"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.theme"
    fi
done

echo "Done."
