#!/usr/bin/env bash
set -euo pipefail

BASE="${XDG_CONFIG_HOME:-$HOME/.jupyter}/lab/themes"
mkdir -p "$BASE"

for f in themes/*.json; do
    name="xscriptor-$(basename "$f" .json)"
    dir="$BASE/$name"
    mkdir -p "$dir"
    cp "$f" "$dir/theme.json"
    cat > "$dir/package.json" <<- EOF
{
  "name": "$name",
  "version": "1.0.0",
  "jupyterlab": {
    "themeDir": ".",
    "type": "theme"
  }
}
EOF
    echo "  \u2713 $name"
done

echo "Done! Jupyter Lab themes installed to $BASE"
