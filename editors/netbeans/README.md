<div align="center">
  <h1>NetBeans Xscriptor</h1>
  <p>ANSI terminal color palettes ported to XML theme files for NetBeans.</p>
</div>

<div align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://netbeans.org"><img src="https://img.shields.io/badge/NetBeans-8.0%2B-blue" alt="NetBeans"></a>
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
      <tr><td><a href="themes/X.xml">X</a></td><td><code>#050505</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Madrid.xml">Madrid</a></td><td><code>#fafafa</code></td><td>light</td></tr>
      <tr><td><a href="themes/Lahabana.xml">Lahabana</a></td><td><code>#19191a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Miami.xml">Miami</a></td><td><code>#000000</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Paris.xml">Paris</a></td><td><code>#1a0a30</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Tokio.xml">Tokio</a></td><td><code>#1c1c1d</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Oslo.xml">Oslo</a></td><td><code>#3f4451</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Helsinki.xml">Helsinki</a></td><td><code>#f8fafe</code></td><td>light</td></tr>
      <tr><td><a href="themes/Berlin.xml">Berlin</a></td><td><code>#000000</code></td><td>dark (monochrome)</td></tr>
      <tr><td><a href="themes/London.xml">London</a></td><td><code>#ffffff</code></td><td>light (monochrome)</td></tr>
      <tr><td><a href="themes/Praha.xml">Praha</a></td><td><code>#1a1a1a</code></td><td>dark</td></tr>
      <tr><td><a href="themes/Bogota.xml">Bogota</a></td><td><code>#200b0a</code></td><td>dark</td></tr>
    </tbody>
  </table>
</div>

<hr>

<h2 id="installation">Installation</h2>

<ol>
  <li><strong>Tools &gt; Options &gt; Font &amp; Colors</strong></li>
  <li>Click <strong>Import</strong> and select the desired <code>.xml</code> file</li>
  <li>Select the imported theme from the profile dropdown</li>
</ol>

<p>To install all themes at once, run:</p>
<pre><code>./install.sh                    # install all themes
./install.sh Praha              # install a single theme
./install.sh -u                 # uninstall all themes</code></pre>

<hr>

<h2 id="generator">Generator</h2>

<p><a href="generate.py"><code>generate.py</code></a> reads <a href="../../colors.json"><code>colors.json</code></a> and produces all XML theme files.</p>

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
