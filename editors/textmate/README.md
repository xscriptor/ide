# TextMate Xscriptor

Xscriptor color themes for TextMate.

## Themes

| Theme | Background |
|-------|------------|
| X | `#050505` |
| Madrid | `#fafafa` |
| Lahabana | `#19191a` |
| Miami | `#000000` |
| Paris | `#1a0a30` |
| Tokio | `#1c1c1d` |
| Oslo | `#3f4451` |
| Helsinki | `#f8fafe` |
| Berlin | `#000000` |
| London | `#ffffff` |
| Praha | `#1a1a1a` |
| Bogota | `#200b0a` |

## Installation

Copy the theme files to the TextMate Themes directory:

```bash
mkdir -p ~/Library/Application\ Support/TextMate/Themes/
cp themes/*.tmTheme ~/Library/Application\ Support/TextMate/Themes/
```

Or use the install script:

```bash
./install.sh          # install all themes
./install.sh Praha    # install a single theme
```

Then restart TextMate and select the theme from **Preferences > Themes**.

## Uninstall

```bash
./uninstall.sh
```

Or manually:

```bash
rm ~/Library/Application\ Support/TextMate/Themes/Xscriptor\ *.tmTheme
```

## Links

- [Repository](https://github.com/xscriptor/ide)
- [Colors](../colors.md)
