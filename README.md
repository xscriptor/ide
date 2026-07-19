<div align="center">
  <h1>IDE</h1>
  <p>Monorepo for editor and IDE X themes/schemes</p>
</div>

<div align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="editors/"><img src="https://img.shields.io/badge/Editors-34-948ae3" alt="Editors: 34"></a>
  <a href="colors.json"><img src="https://img.shields.io/badge/Themes-12-5ad4e6" alt="Themes: 12"></a>
  <a href="https://github.com/xscriptor/ide/releases"><img src="https://img.shields.io/github/v/release/xscriptor/ide?color=fd9353" alt="Release"></a>
  <a href="https://github.com/xscriptor/ide/stargazers"><img src="https://img.shields.io/github/stars/xscriptor/ide?color=fce566" alt="Stars"></a>
  <a href="https://github.com/xscriptor/ide"><img src="https://img.shields.io/github/repo-size/xscriptor/ide?color=7bd88f" alt="Repo size"></a>
  <a href="https://github.com/xscriptor/ide/commits/main"><img src="https://img.shields.io/github/last-commit/xscriptor/ide?color=fc618d" alt="Last commit"></a>
</div>

<hr>

<p>
  This repository contains configurations, themes, and tooling for
  customizing code editors and IDEs. Each editor has its own directory
  with independent projects and documentation.
</p>

<h2>Editors</h2>

<table>
  <thead>
    <tr>
      <th>Editor</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://github.com/xscriptor/vscode">Visual Studio Code</a></td>
      <td>VSCode <code>.vsx</code> extension with full JSON themes, icon themes, and product icon.</td>
    </tr>
    <tr>
      <td><a href="editors/sublime/">Sublime Text</a></td>
      <td>Sublime Text <code>.sublime-color-scheme</code> files for syntax highlighting.</td>
    </tr>
    <tr>
      <td><a href="editors/textmate/">TextMate</a></td>
      <td>TextMate <code>.tmTheme</code> plist XML theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/vim/">Vim</a></td>
      <td>Vim <code>.vim</code> colorscheme files with UI and syntax highlighting.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/xscriptor/nvim">Neovim</a></td>
      <td>Complete Neovim configuration with LSP, DAP, and custom X themes.</td>
    </tr>
    <tr>
      <td><a href="editors/emacs/">Emacs</a></td>
      <td>Emacs <code>deftheme</code> ELisp color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/helix/">Helix</a></td>
      <td>Helix <code>.toml</code> theme files with full syntax highlighting.</td>
    </tr>
    <tr>
      <td><a href="editors/zed/">Zed</a></td>
      <td>Zed <code>.json</code> theme files with syntax and terminal ANSI colors.</td>
    </tr>
    <tr>
      <td><a href="editors/litexl/">Lite XL</a></td>
      <td>Lite XL <code>.lua</code> color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/micro/">Micro</a></td>
      <td>Micro <code>.json</code> colorscheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/geany/">Geany</a></td>
      <td>Geany <code>.scheme</code> color scheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/kate/">Kate</a></td>
      <td>Kate <code>.theme</code> color scheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/gedit/">Gedit</a></td>
      <td>Gedit <code>.xml</code> color scheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/notepadpp/">Notepad++</a></td>
      <td>Notepad++ <code>.xml</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/cudatext/">CudaText</a></td>
      <td>CudaText <code>.json</code> color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/bbedit/">BBEdit</a></td>
      <td>BBEdit <code>.bbcolorproject</code> plist XML color scheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/kakoune/">Kakoune</a></td>
      <td>Kakoune <code>.kak</code> color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/xcode/">Xcode</a></td>
      <td>Xcode <code>.xccolortheme</code> files generated from ANSI terminal palettes.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/xscriptor/jetbrains">JetBrains</a></td>
      <td>JetBrains <code>.zip</code> plugin with full themes for the entire JetBrains suite.</td>
    </tr>
    <tr>
      <td><a href="editors/eclipse/">Eclipse</a></td>
      <td>Eclipse <code>.epf</code> preferences theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/netbeans/">NetBeans</a></td>
      <td>NetBeans <code>.xml</code> font and color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/visualstudio/">Visual Studio</a></td>
      <td>Visual Studio <code>.vssettings</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/qtcreator/">Qt Creator</a></td>
      <td>Qt Creator <code>.creatortheme</code> XML style scheme files.</td>
    </tr>
    <tr>
      <td><a href="editors/codeblocks/">Code::Blocks</a></td>
      <td>Code::Blocks <code>.conf</code> color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/spyder/">Spyder</a></td>
      <td>Spyder <code>.py</code> syntax coloring theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/rstudio/">RStudio</a></td>
      <td>RStudio <code>.tmTheme</code> editor theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/arduino/">Arduino IDE</a></td>
      <td>Arduino IDE 2.x <code>.json</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/lazarus/">Lazarus IDE</a></td>
      <td>Lazarus IDE <code>.xml</code> syntax highlighting theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/codelite/">CodeLite</a></td>
      <td>CodeLite <code>.json</code> color theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/nova/">Nova</a></td>
      <td>Nova <code>.nvatheme</code> JSON theme files with UI and syntax colors.</td>
    </tr>
    <tr>
      <td><a href="editors/replit/">Replit</a></td>
      <td>Replit <code>.json</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/codesandbox/">CodeSandbox</a></td>
      <td>CodeSandbox <code>.json</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="editors/jupyterlab/">Jupyter Lab</a></td>
      <td>Jupyter Lab <code>.json</code> theme files.</td>
    </tr>
    <tr>
      <td><a href="https://github.com/xscriptor/fresh">Fresh</a></td>
      <td>Custom color themes for Fresh, the terminal text editor.</td>
    </tr>
  </tbody>
</table>

<hr>

<div align="center">
<h2>X</h2>

<a href="https://dev.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/verified-filled.svg" width="24" alt="X Web" />
</a>
 & 
<a href="https://github.com/xscriptor">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/github.svg" width="24" alt="X Github Profile" />
</a>
 & 
<a href="https://www.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/quotes.svg" width="24" alt="Xscriptor web" />
</a>
