#!/usr/bin/env bash
set -euo pipefail

echo "CodeSandbox themes are installed via the CodeSandbox UI."
echo ""
echo "1. Open CodeSandbox"
echo "2. Go to Settings > Appearance"
echo "3. Click Import Theme and select a .json file from themes/"
echo ""
echo "Theme files are located in: $(cd "$(dirname "$0")/themes" && pwd)"
echo ""
echo "Themes:"
for f in "$(dirname "$0")"/themes/*.json; do
    echo "  - $(basename "$f")"
done
