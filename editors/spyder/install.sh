#!/usr/bin/env bash
set -euo pipefail

SRC="$(dirname "$0")/themes"

echo "Spyder themes can be imported via:"
echo "  Tools > Preferences > Appearance > Syntax coloring > Import theme"
echo ""
echo "Theme files are located in:"
echo "  $SRC"
echo ""
echo "Alternatively, copy them to Spyder's config directory:"

case "$(uname -s)" in
  Darwin)
    DST="${HOME}/.spyder-py3/syntax_coloring"
    ;;
  Linux)
    DST="${HOME}/.spyder-py3/syntax_coloring"
    ;;
  *)
    echo "Unsupported OS: $(uname -s)" >&2
    exit 1
    ;;
esac

mkdir -p "$DST"

for theme in "$SRC"/*.py; do
    cp "$theme" "$DST/"
    echo "  installed $(basename "$theme")"
done

echo "Done. All themes copied to $DST"
