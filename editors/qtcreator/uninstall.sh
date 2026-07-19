#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.config/QtProject/qtcreator/styles"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.creatortheme"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.creatortheme"
    fi
done

echo "Done."
