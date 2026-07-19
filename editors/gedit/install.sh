#!/usr/bin/env bash
set -euo pipefail

SRC="$(dirname "$0")/themes"
DST="${HOME}/.local/share/gedit/styles"

mkdir -p "$DST"

for theme in "$SRC"/*.xml; do
    cp "$theme" "$DST/"
    echo "  installed $(basename "$theme")"
done

echo "Done. All themes copied to $DST"
