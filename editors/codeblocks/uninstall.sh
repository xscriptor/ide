#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.local/share/codeblocks/themes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.conf"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.conf"
    fi
done

echo "Done."
