#!/usr/bin/env bash
set -euo pipefail

SRC="$(dirname "$0")/themes"
DST="${HOME}/.config/geany/colorschemes"

mkdir -p "$DST"

for theme in "$SRC"/*.scheme; do
    cp "$theme" "$DST/"
    echo "  installed $(basename "$theme")"
done

echo "Done. All themes copied to $DST"
