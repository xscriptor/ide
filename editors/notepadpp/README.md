# Notepad++ Xscriptor

Color themes for the [Notepad++](https://notepad-plus-plus.org/) editor, generated from the Xscriptor palette collection.

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

### Windows

```powershell
copy themes\*.xml "%APPDATA%\Notepad++\themes\"
```

Or run the install script (Linux/WSL):

```bash
./install.sh
```

### Linux (Wine)

```bash
cp themes/*.xml "$HOME/.wine/drive_c/users/$USER/AppData/Roaming/Notepad++/themes/"
```

## Usage

Select the theme in Notepad++ via **Settings > Style Configurator > Select theme**.

## Uninstall

```bash
./uninstall.sh
```
