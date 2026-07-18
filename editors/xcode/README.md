<div align="center">
  <h1>Xcode Xscriptor</h1>
  <p>Convert ANSI terminal color palettes (16 colors per palette, 12 palettes) to <code>.xccolortheme</code> files for Xcode.</p>
</div>

<div align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://developer.apple.com/xcode/"><img src="https://img.shields.io/badge/Xcode-12%2B-blue" alt="Xcode"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python"></a>
  <a href="#themes"><img src="https://img.shields.io/badge/Themes-12-purple" alt="Themes"></a>
</div>

<hr>

<h2>Content</h2>

<ul>
  <li><a href="#overview">Overview</a></li>
  <li><a href="#themes">Themes</a></li>
  <li><a href="#usage">Usage</a></li>
  <li><a href="#installation">Installation</a></li>
  <li><a href="#related-documents">Related Documents</a></li>
  <li><a href="#license">License</a></li>
  <li><a href="#x">X</a></li>
</ul>

<hr>

<h2 id="overview">Overview</h2>

<p>
  This generator reads ANSI terminal palettes (16 colors each, 12 palettes) defined in
  <a href="colors.md"><code>colors.md</code></a> and produces Xcode
  <code>.xccolortheme</code> files. Each palette maps to 24 Xcode syntax
  tokens (keywords, strings, comments, types, etc.) so that the editor's
  syntax highlighting matches the terminal color scheme.
</p>

<p>
  Canonical themes live in <a href="themes/"><code>themes/</code></a>.
  When the source palette changes, run the generator to rebuild them into
  <a href="labs/dist/"><code>labs/dist/</code></a>.
</p>

<hr>

<h2 id="themes">Themes</h2>

<div align="center">
  <table>
    <thead>
      <tr>
        <th>Theme</th>
        <th>Background</th>
        <th>Type</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><a href="themes/X.xccolortheme">X</a></td><td><code>#050505</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Madrid.xccolortheme">Madrid</a></td><td><code>#fafafa</code></td><td>light</td></tr>
      <tr><td><a href="themes/Lahabana.xccolortheme">Lahabana</a></td><td><code>#19191a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Miami.xccolortheme">Miami</a></td><td><code>#000000</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Paris.xccolortheme">Paris</a></td><td><code>#1a0a30</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Tokio.xccolortheme">Tokio</a></td><td><code>#1c1c1d</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Oslo.xccolortheme">Oslo</a></td><td><code>#3f4451</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Helsinki.xccolortheme">Helsinki</a></td><td><code>#f8fafe</code></td><td>light</td></tr>
      <tr><td><a href="themes/Berlin.xccolortheme">Berlin</a></td><td><code>#000000</code></td><td>dark (monochrome)</td></tr>
      <tr><td><a href="themes/London.xccolortheme">London</a></td><td><code>#ffffff</code></td><td>light (monochrome)</td></tr>
      <tr><td><a href="themes/Praha.xccolortheme">Praha</a></td><td><code>#1a1a1a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Bogota.xccolortheme">Bogota</a></td><td><code>#200b0a</code></td><td>dark</td></tr>
    </tbody>
  </table>
</div>

<hr>

<h2 id="usage">Usage</h2>

<pre><code>cd labs
python3 generate_themes.py</code></pre>

<p>All <code>.xccolortheme</code> files are written to <code>labs/dist/</code>. Once tested, promote them to <code>themes/</code> if desired.</p>

<h3>Programmatic API</h3>

<pre><code>from labs.generate_themes import make_theme, THEMES, SYNTAX_MAP

theme = THEMES["Praha"]
colors = make_theme("Praha", theme)</code></pre>

<hr>

<hr>

<h2 id="installation">Installation</h2>

<h3>Local</h3>

<pre><code>./install.sh              # install all themes
./install.sh Praha        # install a single theme</code></pre>

<h3>Remote (from GitHub)</h3>

<pre><code>REPO="xscriptor/xcode" bash &lt;(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh)</code></pre>

<p>Install a single theme remotely:</p>

<pre><code>REPO="xscriptor/xcode" bash &lt;(curl -fsSL https://raw.githubusercontent.com/xscriptor/xcode/main/install.sh) -s Praha</code></pre>

<h3>Uninstall</h3>

<pre><code>./install.sh -u                                      # local uninstall
REPO="xscriptor/xcode" bash &lt;(curl -fsSL ...) -s -- -u   # remote uninstall</code></pre>

<p>This removes any theme file matching the known theme names from <code>~/Library/Developer/Xcode/UserData/FontAndColorThemes/</code>.</p>

<p>After installation, restart Xcode and select the theme from <strong>Xcode &gt; Preferences &gt; Themes</strong>.</p>

<hr>

<h2 id="related-documents">Related Documents</h2>

<ul>
  <li id="colors-md"><a href="colors.md">colors.md</a></li>
  <li id="contributing-md"><a href="CONTRIBUTING.md">CONTRIBUTING.md</a></li>
  <li id="security-md"><a href="SECURITY.md">SECURITY.md</a></li>
  <li id="code-of-conduct-md"><a href="CODE_OF_CONDUCT.md">CODE_OF_CONDUCT.md</a></li>
  <li id="color-mapping-md"><a href="docs/color-mapping.md">docs/color-mapping.md</a></li>
  <li id="labs-readme"><a href="labs/README.md">labs/README.md</a></li>
  <li id="license"><a href="LICENSE.md">labs/README.md</a></li>
</ul>

<hr>



<div id="x" align="center">
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

</div>
