<div align="center">
  <h1>Xcode Theme Generator</h1>
  <p>Convert ANSI 16-color terminal palettes to <code>.xccolortheme</code> files for Xcode.</p>
</div>

<div align="center">

  [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![Xcode](https://img.shields.io/badge/Xcode-12%2B-blue)](https://developer.apple.com/xcode/)
  [![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://python.org)
  [![Themes](https://img.shields.io/badge/Themes-12-purple)](#themes)

</div>

---

## Table of Contents

- [Overview](#overview)
- [Themes](#themes)
- [Usage](#usage)
- [Color Mapping](#color-mapping)
- [Installation](#installation)
- [Contributing](#contributing)
- [Security](#security)
- [Code of Conduct](#code-of-conduct)
- [Project Structure](#project-structure)
- [License](#license)

---

## Overview

This generator reads ANSI 16-color terminal palettes defined in [`colors.md`](colors.md) and produces Xcode `.xccolortheme` files. Each palette maps to 24 Xcode syntax tokens (keywords, strings, comments, types, etc.) so that the editor's syntax highlighting matches the terminal color scheme.

Canonical themes live in [`themes/`](themes/). When the source palette changes, run the generator to rebuild them into [`labs/dist/`](labs/dist/).

---

## Themes

<div align="center">

| Theme | Background | Type |
|-------|-----------|------|
| [X](themes/X.xccolortheme) | `#050505` | dark |
| [Madrid](themes/Madrid.xccolortheme) | `#fafafa` | light |
| [Lahabana](themes/Lahabana.xccolortheme) | `#19191a` | dark |
| [Miami](themes/Miami.xccolortheme) | `#000000` | dark |
| [Paris](themes/Paris.xccolortheme) | `#1a0a30` | dark |
| [Tokio](themes/Tokio.xccolortheme) | `#1c1c1d` | dark |
| [Oslo](themes/Oslo.xccolortheme) | `#3f4451` | dark |
| [Helsinki](themes/Helsinki.xccolortheme) | `#f8fafe` | light |
| [Berlin](themes/Berlin.xccolortheme) | `#000000` | dark (monochrome) |
| [London](themes/London.xccolortheme) | `#ffffff` | light (monochrome) |
| [Praha](themes/Praha.xccolortheme) | `#1a1a1a` | dark |
| [Bogota](themes/Bogota.xccolortheme) | `#200b0a` | dark |

</div>

---

## Usage

```bash
cd labs
python3 generate_themes.py
```

All `.xccolortheme` files are written to `labs/dist/`. Once tested, promote them to `themes/` if desired.

### Programmatic API

```python
from labs.generate_themes import make_theme, THEMES, SYNTAX_MAP

theme = THEMES["Praha"]
colors = make_theme("Praha", theme)
```

---

## Color Mapping

Each ANSI palette index is mapped to specific Xcode syntax tokens:

<div align="center">

| ANSI Index | Example Use | Xcode Syntax Key |
|-----------|-------------|-----------------|
| `foreground` | default text | `xcode.syntax.plain` |
| `color0` | -- | -- |
| `color1` | character literals | `xcode.syntax.character` |
| `color2` | comments | `xcode.syntax.comment`, `xcode.syntax.comment.keyword`, `xcode.syntax.mark` |
| `color3` | numbers, system constants | `xcode.syntax.number`, `xcode.syntax.identifier.constant.system` |
| `color4` | functions, attributes | `xcode.syntax.identifier.function`, `xcode.syntax.attribute` |
| `color5` | keywords | `xcode.syntax.keyword` |
| `color6` | classes, types | `xcode.syntax.identifier.class`, `xcode.syntax.identifier.type` |
| `color7` | variables | `xcode.syntax.identifier.variable` |
| `color8` | -- | -- |
| `color9` | strings | `xcode.syntax.string` |
| `color10` | doc comments | `xcode.syntax.comment.doc`, `xcode.syntax.comment.doc.keyword`, `xcode.syntax.markup.code` |
| `color11` | constants | `xcode.syntax.identifier.constant` |
| `color12` | URLs | `xcode.syntax.url` |
| `color13` | preprocessor, macros, project | `xcode.syntax.preprocessor`, `xcode.syntax.identifier.macro`, `xcode.syntax.project` |
| `color14` | system classes | `xcode.syntax.identifier.class.system` |
| `color15` | -- | -- |

</div>

Palette values are used directly without blending. Background-derived colors (current line highlight, selection, insertion point) are adjusted automatically based on luminance.

---

## Installation

### Local

```bash
./install.sh              # install all themes
./install.sh Praha        # install a single theme
```

### Remote (from GitHub)

```bash
REPO="xscriptor/xcode" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh)
```

Install a single theme remotely:

```bash
REPO="xscriptor/xcode" bash <(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh) -s Praha
```

### Uninstall

```bash
./install.sh -u                                      # local uninstall
REPO="xscriptor/xcode" bash <(curl -fsSL ...) -s -- -u   # remote uninstall
```

This removes any theme file matching the known theme names from `~/Library/Developer/Xcode/UserData/FontAndColorThemes/`.

After installation, restart Xcode and select the theme from **Xcode > Preferences > Themes**.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Security

See [SECURITY.md](SECURITY.md).

---

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

---

## Project Structure

```
.
├── README.md                 -- This file
├── CONTRIBUTING.md           -- Contribution guidelines
├── SECURITY.md               -- Security policy
├── CODE_OF_CONDUCT.md        -- Code of conduct
├── .gitignore                -- Git ignore rules
├── install.sh                -- macOS install script
├── colors.md                 -- Source ANSI color definitions
│
├── themes/                   -- Canonical theme files (tracked)
│   ├── Praha.xccolortheme
│   ├── Madrid.xccolortheme
│   └── ...
│
└── labs/
    ├── generate_themes.py    -- Theme generator script
    ├── dist/                 -- Generated themes (gitignored)
    │   ├── Praha.xccolortheme
    │   ├── Madrid.xccolortheme
    │   └── ...
    └── README.md             -- Generator-specific docs
```

---

## License

MIT
