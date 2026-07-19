#!/usr/bin/env bash
set -euo pipefail

DST="${HOME}/.spyder-py3/syntax_coloring"

for theme in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
    file="$DST/${theme}.py"
    if [ -f "$file" ]; then
        rm "$file"
        echo "  removed ${theme}.py"
    fi
done

echo "Done."
