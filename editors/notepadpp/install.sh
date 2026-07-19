#!/usr/bin/env bash
set -euo pipefail

SRC="$(dirname "$0")/themes"
DST="${HOME}/.wine/drive_c/users/${USER}/AppData/Roaming/Notepad++/themes"

mkdir -p "$DST"

for theme in "$SRC"/*.xml; do
    cp "$theme" "$DST/"
    echo "  installed $(basename "$theme")"
done

echo "Done. All themes copied to $DST"
