#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.arduino15/themes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.json"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.json"
    fi
done

echo "Done."
