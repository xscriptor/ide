#!/usr/bin/env bash
set -euo pipefail

if [[ -d "${HOME}/.config/emacs" ]]; then
    THEME_DIR="${HOME}/.config/emacs/themes"
else
    THEME_DIR="${HOME}/.emacs.d/themes"
fi

mkdir -p "$THEME_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for f in "$SCRIPT_DIR"/themes/xscriptor-*.el; do
    cp "$f" "$THEME_DIR/"
    echo "  Installed $(basename "$f")"
done

echo "Done. All Xscriptor themes copied to $THEME_DIR"
