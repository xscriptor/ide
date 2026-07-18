<div align="center">
  <h1>Theme Generator</h1>
  <p>Script that converts ANSI color palettes into <code>.xccolortheme</code> files.</p>
</div>

<hr>

<h2 id="overview">Overview</h2>

<p>
  <code>generate_themes.py</code> reads the palettes defined in
  <a href="../../colors.md"><code>colors.md</code></a> and produces
  Xcode theme files in <code>dist/</code>.
  Each theme maps the 16 ANSI colors to 24 Xcode syntax tokens.
</p>

<p>See the <a href="../../README.md">root README</a> for installation instructions and theme listing.</p>

<hr>

<h2 id="usage">Usage</h2>

<pre><code>python3 generate_themes.py</code></pre>

<p>Output is written to <code>dist/</code>.</p>

<h3>Adding a new palette</h3>

<ol>
  <li>Add your JSON block to <code>../../colors.md</code> with keys <code>color0</code> through <code>color15</code>, <code>background</code>, and <code>foreground</code>.</li>
  <li>Add an entry in <code>THEMES</code> dict inside <code>generate_themes.py</code>.</li>
  <li>Run the script to generate the new <code>.xccolortheme</code> file.</li>
</ol>

<hr>

<h2 id="api">Programmatic API</h2>

<pre><code>from generate_themes import make_theme, THEMES, SYNTAX_MAP

# Access raw palette
theme = THEMES["Praha"]

# Build plist-ready dict
colors = make_theme("Praha", theme)</code></pre>

<h3>Functions</h3>

<ul>
  <li><code>make_theme(name, colors)</code> -- Returns an <code>OrderedDict</code> ready for <code>plistlib.dumps()</code>.</li>
  <li><code>hex_to_rgba(h)</code> -- Converts <code>#rrggbb</code> to <code>[r, g, b, a]</code> floats.</li>
  <li><code>is_light(bg)</code> -- Returns <code>True</code> if background luminance &gt; 0.5.</li>
</ul>

<h3>Constants</h3>

<ul>
  <li><code>THEMES</code> -- <code>dict</code> of theme name to palette dict.</li>
  <li><code>SYNTAX_MAP</code> -- <code>list</code> of <code>(xcode_key, ansi_index)</code> tuples.</li>
</ul>

<hr>

<h2 id="color-mapping">Color Mapping</h2>

<p>The <code>SYNTAX_MAP</code> tuple list defines how ANSI indices map to Xcode syntax keys:</p>

<table>
  <thead>
    <tr>
      <th>ANSI Index</th>
      <th>Xcode Syntax Keys</th>
    </tr>
  </thead>
  <tbody>
    <tr><td><code>foreground</code></td><td><code>xcode.syntax.plain</code></td></tr>
    <tr><td><code>color1</code></td><td><code>xcode.syntax.character</code></td></tr>
    <tr><td><code>color2</code></td><td><code>xcode.syntax.comment</code>, <code>xcode.syntax.comment.keyword</code>, <code>xcode.syntax.mark</code></td></tr>
    <tr><td><code>color3</code></td><td><code>xcode.syntax.number</code>, <code>xcode.syntax.identifier.constant.system</code></td></tr>
    <tr><td><code>color4</code></td><td><code>xcode.syntax.identifier.function</code>, <code>xcode.syntax.attribute</code></td></tr>
    <tr><td><code>color5</code></td><td><code>xcode.syntax.keyword</code></td></tr>
    <tr><td><code>color6</code></td><td><code>xcode.syntax.identifier.class</code>, <code>xcode.syntax.identifier.type</code></td></tr>
    <tr><td><code>color7</code></td><td><code>xcode.syntax.identifier.variable</code></td></tr>
    <tr><td><code>color9</code></td><td><code>xcode.syntax.string</code></td></tr>
    <tr><td><code>color10</code></td><td><code>xcode.syntax.comment.doc</code>, <code>xcode.syntax.comment.doc.keyword</code>, <code>xcode.syntax.markup.code</code></td></tr>
    <tr><td><code>color11</code></td><td><code>xcode.syntax.identifier.constant</code></td></tr>
    <tr><td><code>color12</code></td><td><code>xcode.syntax.url</code></td></tr>
    <tr><td><code>color13</code></td><td><code>xcode.syntax.preprocessor</code>, <code>xcode.syntax.identifier.macro</code>, <code>xcode.syntax.project</code></td></tr>
    <tr><td><code>color14</code></td><td><code>xcode.syntax.identifier.class.system</code></td></tr>
  </tbody>
</table>

<p>Indices <code>color0</code>, <code>color8</code>, and <code>color15</code> are unused.</p>

<hr>

<h2 id="output">Output format</h2>

<p>
  Each generated <code>.xccolortheme</code> is a standard Apple XML plist with
  <code>DVTSourceTextBackground</code>, <code>DVTSourceTextSyntaxColors</code>,
  <code>DVTSourceTextSyntaxFonts</code>, and related keys.
  Font is set to <code>SFMono-Regular - 12.0</code> for all syntax tokens.
</p>

<hr>

<p><a href="../../README.md">Back to root README</a></p>
