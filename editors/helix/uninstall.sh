#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.config/helix/themes"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.toml"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.toml"
    fi
done

echo "Done."
