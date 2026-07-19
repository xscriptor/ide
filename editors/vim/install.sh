#!/usr/bin/env bash
set -euo pipefail

THEME_DIR="${HOME}/.vim/colors"
mkdir -p "$THEME_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for f in "$SCRIPT_DIR"/themes/*.vim; do
    cp "$f" "$THEME_DIR/"
    echo "  Installed $(basename "$f")"
done

echo "Done. All Xscriptor themes copied to $THEME_DIR"
