# Helix Xscriptor

Color themes for the [Helix](https://helix-editor.com/) editor, generated from the Xscriptor palette collection.

## Themes

| Name      | Type    |
|-----------|---------|
| X         | dark    |
| Madrid    | light   |
| Lahabana  | dark    |
| Miami     | dark    |
| Paris     | dark    |
| Tokio     | dark    |
| Oslo      | dark    |
| Helsinki  | light   |
| Berlin    | dark    |
| London    | light   |
| Praha     | dark    |
| Bogota    | dark    |

## Installation

Copy themes to the Helix config directory:

```bash
cp themes/*.toml ~/.config/helix/themes/
```

Or run the install script:

```bash
./install.sh
```

## Usage

Set the theme in `~/.config/helix/config.toml`:

```toml
theme = "X"
```

Replace `X` with any theme name from the table above.

## Uninstall

```bash
./uninstall.sh
```
