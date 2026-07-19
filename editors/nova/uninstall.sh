#!/usr/bin/env bash
set -euo pipefail

THEME_DIR="${HOME}/Library/Application Support/Nova/Themes"

if ls "$THEME_DIR"/"Xscriptor"*.nvatheme &>/dev/null; then
    for name in X Madrid Lahabana Miami Paris Tokio Oslo Helsinki Berlin London Praha Bogota; do
        if [[ -f "$THEME_DIR/Xscriptor ${name}.nvatheme" ]]; then
            rm "$THEME_DIR/Xscriptor ${name}.nvatheme"
            echo "  Removed Xscriptor ${name}.nvatheme"
        fi
    done
    echo "Done. Xscriptor themes removed from $THEME_DIR"
else
    echo "No Xscriptor themes found in $THEME_DIR"
fi
