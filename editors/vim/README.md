# Xscriptor Vim Colorschemes

12 color themes for Vim, generated from [colors.json](../../colors.json).

## Installation

Copy the `.vim` files to your `~/.vim/colors/` directory:

```bash
# Option 1: Copy all themes
cp dist/*.vim ~/.vim/colors/

# Option 2: Use the install script
chmod +x install.sh
./install.sh
```

## Usage

Add to your `~/.vimrc`:

```vim
colorscheme xscriptor_madrid
```

Available themes: `x`, `madrid`, `lahabana`, `miami`, `paris`, `tokio`, `oslo`, `helsinki`, `berlin`, `london`, `praha`, `bogota`.

## Uninstall

```bash
./uninstall.sh
# or
rm ~/.vim/colors/xscriptor_*.vim
```

## Regeneration

```bash
python3 generate.py
```
