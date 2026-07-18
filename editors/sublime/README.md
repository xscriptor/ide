<div align="center">
  <h1>Sublime Text Xscriptor</h1>
  <p>ANSI terminal color palettes ported to <code>.sublime-color-scheme</code> files for Sublime Text.</p>
</div>

<div align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.sublimetext.com"><img src="https://img.shields.io/badge/Sublime%20Text-3.1%2B-blue" alt="Sublime Text"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python"></a>
  <a href="#themes"><img src="https://img.shields.io/badge/Themes-12-purple" alt="Themes"></a>
</div>

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
      <tr><td><a href="themes/X.sublime-color-scheme">X</a></td><td><code>#050505</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Madrid.sublime-color-scheme">Madrid</a></td><td><code>#fafafa</code></td><td>light</td></tr>
      <tr><td><a href="themes/Lahabana.sublime-color-scheme">Lahabana</a></td><td><code>#19191a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Miami.sublime-color-scheme">Miami</a></td><td><code>#000000</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Paris.sublime-color-scheme">Paris</a></td><td><code>#1a0a30</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Tokio.sublime-color-scheme">Tokio</a></td><td><code>#1c1c1d</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Oslo.sublime-color-scheme">Oslo</a></td><td><code>#3f4451</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Helsinki.sublime-color-scheme">Helsinki</a></td><td><code>#f8fafe</code></td><td>light</td></tr>
      <tr><td><a href="themes/Berlin.sublime-color-scheme">Berlin</a></td><td><code>#000000</code></td><td>dark (monochrome)</td></tr>
      <tr><td><a href="themes/London.sublime-color-scheme">London</a></td><td><code>#ffffff</code></td><td>light (monochrome)</td></tr>
      <tr><td><a href="themes/Praha.sublime-color-scheme">Praha</a></td><td><code>#1a1a1a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Bogota.sublime-color-scheme">Bogota</a></td><td><code>#200b0a</code></td><td>dark</td></tr>
    </tbody>
  </table>
</div>

<hr>

<h2 id="installation">Installation</h2>

<pre><code>./install.sh                    # install all themes
./install.sh Praha              # install a single theme
./install.sh -u                 # uninstall all themes</code></pre>

<p>After installation, select the theme from <strong>Preferences &gt; Color Scheme</strong> in Sublime Text.</p>

<hr>

<h2 id="generator">Generator</h2>

<p><a href="generate.py"><code>generate.py</code></a> reads <a href="../../colors.json"><code>colors.json</code></a> and produces all <code>.sublime-color-scheme</code> files.</p>

<pre><code>python3 generate.py</code></pre>

<hr>

<div align="center">
  <a href="https://dev.xscriptor.com">
    <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/verified-filled.svg" width="24" alt="X Web" />
  </a>
  &amp;
  <a href="https://github.com/xscriptor">
    <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/github.svg" width="24" alt="X Github Profile" />
  </a>
  &amp;
  <a href="https://www.xscriptor.com">
    <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/quotes.svg" width="24" alt="Xscriptor web" />
  </a>
</div>
