#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.config/geany/colorschemes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.scheme"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.scheme"
    fi
done

echo "Done."
