# Xscriptor Themes for Lite XL

## Install

```bash
./install.sh
```

Or manually copy `.lua` files to `~/.config/lite-xl/colors/`.

## Uninstall

```bash
./uninstall.sh
```

## Usage

In your `init.lua`, add:

```lua
core.reload_module("colors.xscriptor-<name>")
```

Replace `<name>` with one of: x, madrid, lahabana, miami, paris, tokio, oslo, helsinki, berlin, london, praha, bogota.
