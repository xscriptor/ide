#!/usr/bin/env bash
set -euo pipefail

if [[ -d "${HOME}/.config/emacs/themes" ]]; then
    THEME_DIR="${HOME}/.config/emacs/themes"
else
    THEME_DIR="${HOME}/.emacs.d/themes"
fi

if ls "$THEME_DIR"/xscriptor-*.el &>/dev/null; then
    rm "$THEME_DIR"/xscriptor-*.el
    echo "Removed all Xscriptor themes from $THEME_DIR"
else
    echo "No Xscriptor themes found in $THEME_DIR"
fi
