# Xscriptor Kakoune Themes

12 color themes for Kakoune, generated from [colors.json](../../colors.json).

## Installation

Copy the `.kak` files to your Kakoune colors directory:

```bash
# Option 1: Use the install script
chmod +x install.sh
./install.sh

# Option 2: Manual copy
cp themes/*.kak ~/.config/kak/colors/
```

## Usage

In your `~/.config/kak/kakrc`:

```kak
colorscheme madrid
```

Available themes: `X`, `Madrid`, `Lahabana`, `Miami`, `Paris`, `Tokio`, `Oslo`, `Helsinki`, `Berlin`, `London`, `Praha`, `Bogota`.

## Uninstall

```bash
./uninstall.sh
```

## Regeneration

```bash
python3 generate.py
```
