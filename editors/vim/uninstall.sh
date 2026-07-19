#!/usr/bin/env bash
set -euo pipefail

THEME_DIR="${HOME}/.vim/colors"

if ls "$THEME_DIR"/xscriptor_*.vim &>/dev/null; then
    rm "$THEME_DIR"/xscriptor_*.vim
    echo "Removed all Xscriptor themes from $THEME_DIR"
else
    echo "No Xscriptor themes found in $THEME_DIR"
fi
