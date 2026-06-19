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
- [Project Structure](#project-structure)
- [License](#license)

---

## Overview

This generator reads ANSI 16-color terminal palettes defined in `colors.md` and produces Xcode `.xccolortheme` files. Each palette maps to 24 Xcode syntax tokens (keywords, strings, comments, types, etc.) so that the editor's syntax highlighting matches the terminal color scheme.

Themes are exported to [`dist/`](dist/) and can be installed directly into Xcode.

---

## Themes

<div align="center">

| Theme | Background | Type |
|-------|-----------|------|
| [X](dist/X.xccolortheme) | `#050505` | dark |
| [Madrid](dist/Madrid.xccolortheme) | `#fafafa` | light |
| [Lahabana](dist/Lahabana.xccolortheme) | `#19191a` | dark |
| [Miami](dist/Miami.xccolortheme) | `#000000` | dark |
| [Paris](dist/Paris.xccolortheme) | `#1a0a30` | dark |
| [Tokio](dist/Tokio.xccolortheme) | `#1c1c1d` | dark |
| [Oslo](dist/Oslo.xccolortheme) | `#3f4451` | dark |
| [Helsinki](dist/Helsinki.xccolortheme) | `#f8fafe` | light |
| [Berlin](dist/Berlin.xccolortheme) | `#000000` | dark (monochrome) |
| [London](dist/London.xccolortheme) | `#ffffff` | light (monochrome) |
| [Praha](dist/Praha.xccolortheme) | `#1a1a1a` | dark |
| [Bogota](dist/Bogota.xccolortheme) | `#200b0a` | dark |

</div>

---

## Usage

```bash
python3 generate_themes.py
```

All `.xccolortheme` files are written to the `dist/` directory.

### Programmatic API

```python
from generate_themes import make_theme, THEMES, SYNTAX_MAP

# Access raw theme data
theme = THEMES["Praha"]           # dict with background, foreground, color0..color15
colors = make_theme("Praha", theme)  # ready-to-serialize plist dict
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
| `color3` | numbers | `xcode.syntax.number`, `xcode.syntax.identifier.constant.system` |
| `color4` | functions, attributes | `xcode.syntax.identifier.function`, `xcode.syntax.attribute` |
| `color5` | keywords | `xcode.syntax.keyword` |
| `color6` | classes, types | `xcode.syntax.identifier.class`, `xcode.syntax.identifier.type` |
| `color7` | variables | `xcode.syntax.identifier.variable` |
| `color8` | -- | -- |
| `color9` | strings | `xcode.syntax.string` |
| `color10` | doc comments | `xcode.syntax.comment.doc`, `xcode.syntax.comment.doc.keyword`, `xcode.syntax.markup.code` |
| `color11` | constants | `xcode.syntax.identifier.constant` |
| `color12` | URLs | `xcode.syntax.url` |
| `color13` | preprocessor, macros | `xcode.syntax.preprocessor`, `xcode.syntax.identifier.macro`, `xcode.syntax.project` |
| `color14` | system classes/types | `xcode.syntax.identifier.class.system`, `xcode.syntax.identifier.type` (duplicate mapping) |
| `color15` | -- | -- |

</div>

The palette index and foreground color are used directly; no blending or interpolation is applied to syntax colors. Background-derived colors (current line highlight, selection, insertion point) are adjusted automatically based on luminance.

---

## Installation

Copy the theme files into Xcode's `FontAndColorThemes` directory:

```bash
cp dist/*.xccolortheme ~/Library/Developer/Xcode/UserData/FontAndColorThemes/
```

Restart Xcode, then select the theme from:

**Xcode > Preferences > Themes**

The theme name will appear in the list matching the filename (e.g. `Praha` for `Praha.xccolortheme`).

---

## Project Structure

```
labs/
  generate_themes.py    -- Theme generator script
  README.md             -- This file
  dist/                 -- Compiled .xccolortheme files
    Praha.xccolortheme
    Madrid.xccolortheme
    ...
colors.md               -- Source ANSI color definitions (root)
```

---

## License

MIT
