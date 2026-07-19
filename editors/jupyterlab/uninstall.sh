#!/usr/bin/env bash
set -euo pipefail

BASE="${XDG_CONFIG_HOME:-$HOME/.jupyter}/lab/themes"

echo "Removing Xscriptor Jupyter Lab themes..."
for f in themes/*.json; do
    name="xscriptor-$(basename "$f" .json)"
    rm -rf "$BASE/$name"
done
echo "Done."
