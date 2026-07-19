# Xscriptor Emacs Themes

12 color themes for Emacs, generated from [colors.json](../../colors.json).

## Installation

Copy the `.el` files to your Emacs themes directory:

```bash
# Option 1: Use the install script
chmod +x install.sh
./install.sh

# Option 2: Manual copy
cp themes/*.el ~/.emacs.d/themes/
# or
cp themes/*.el ~/.config/emacs/themes/
```

## Usage

Add to your `~/.emacs.d/init.el` or `~/.config/emacs/init.el`:

```elisp
(load-theme 'xscriptor-madrid t)
```

Available themes: `xscriptor-x`, `xscriptor-madrid`, `xscriptor-lahabana`, `xscriptor-miami`, `xscriptor-paris`, `xscriptor-tokio`, `xscriptor-oslo`, `xscriptor-helsinki`, `xscriptor-berlin`, `xscriptor-london`, `xscriptor-praha`, `xscriptor-bogota`.

## Uninstall

```bash
./uninstall.sh
```

## Regeneration

```bash
python3 generate.py
```
