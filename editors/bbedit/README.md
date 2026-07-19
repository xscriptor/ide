# Xscriptor BBEdit Themes

12 color themes for BBEdit, generated from [colors.json](../../colors.json).

## Installation

Copy the `.bbcolorproject` files to your BBEdit Color Schemes directory:

```bash
# Option 1: Use the install script
chmod +x install.sh
./install.sh

# Option 2: Manual copy
cp themes/*.bbcolorproject ~/Library/Application\ Support/BBEdit/Color\ Schemes/
```

## Usage

1. Open BBEdit
2. Go to **Preferences > Editor Colors**
3. Select a theme from the dropdown

Available themes: X, Madrid, Lahabana, Miami, Paris, Tokio, Oslo, Helsinki, Berlin, London, Praha, Bogota.

## Uninstall

```bash
./uninstall.sh
```

## Regeneration

```bash
python3 generate.py
```
