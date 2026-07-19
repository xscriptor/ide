#!/usr/bin/env bash
set -euo pipefail

THEME_DIR="${HOME}/.config/kak/colors"

if ls "$THEME_DIR"/*.kak &>/dev/null; then
    # Only remove files that match our theme names
    for name in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
        if [[ -f "$THEME_DIR/${name}.kak" ]]; then
            rm "$THEME_DIR/${name}.kak"
            echo "  Removed ${name}.kak"
        fi
    done
    echo "Done. Xscriptor themes removed from $THEME_DIR"
else
    echo "No Xscriptor themes found in $THEME_DIR"
fi
