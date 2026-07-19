#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.config/rstudio/themes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.tmTheme"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.tmTheme"
    fi
done

echo "Done."
