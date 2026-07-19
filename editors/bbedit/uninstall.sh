#!/usr/bin/env bash
set -euo pipefail

THEME_DIR="${HOME}/Library/Application Support/BBEdit/Color Schemes"

if ls "$THEME_DIR"/*.bbcolorproject &>/dev/null; then
    for name in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
        if [[ -f "$THEME_DIR/${name}.bbcolorproject" ]]; then
            rm "$THEME_DIR/${name}.bbcolorproject"
            echo "  Removed ${name}.bbcolorproject"
        fi
    done
    echo "Done. Xscriptor themes removed from $THEME_DIR"
else
    echo "No Xscriptor themes found in $THEME_DIR"
fi
