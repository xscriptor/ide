<div align="center">
  <h1>Color Mapping</h1>
  <p>How ANSI 16-color palette indices map to Xcode syntax tokens.</p>
</div>

<hr>

<p>
  Each palette defined in <a href="../../colors.md"><code>colors.md</code></a>
  contains 16 ANSI colors (<code>color0</code> through <code>color15</code>)
  plus <code>background</code> and <code>foreground</code>.
  The generator maps them to Xcode syntax tokens as follows:
</p>

<div align="center">
  <table>
    <thead>
      <tr>
        <th>Source</th>
        <th>Example Use</th>
        <th>Xcode Syntax Key</th>
      </tr>
    </thead>
    <tbody>
      <tr><td><code>foreground</code></td><td>default text</td><td><code>xcode.syntax.plain</code></td></tr>
      <tr><td><code>color0</code></td><td>--</td><td>--</td></tr>
      <tr><td><code>color1</code></td><td>character literals</td><td><code>xcode.syntax.character</code></td></tr>
      <tr><td><code>color2</code></td><td>comments</td><td><code>xcode.syntax.comment</code>, <code>xcode.syntax.comment.keyword</code>, <code>xcode.syntax.mark</code></td></tr>
      <tr><td><code>color3</code></td><td>numbers, system constants</td><td><code>xcode.syntax.number</code>, <code>xcode.syntax.identifier.constant.system</code></td></tr>
      <tr><td><code>color4</code></td><td>functions, attributes</td><td><code>xcode.syntax.identifier.function</code>, <code>xcode.syntax.attribute</code></td></tr>
      <tr><td><code>color5</code></td><td>keywords</td><td><code>xcode.syntax.keyword</code></td></tr>
      <tr><td><code>color6</code></td><td>classes, types</td><td><code>xcode.syntax.identifier.class</code>, <code>xcode.syntax.identifier.type</code></td></tr>
      <tr><td><code>color7</code></td><td>variables</td><td><code>xcode.syntax.identifier.variable</code></td></tr>
      <tr><td><code>color8</code></td><td>--</td><td>--</td></tr>
      <tr><td><code>color9</code></td><td>strings</td><td><code>xcode.syntax.string</code></td></tr>
      <tr><td><code>color10</code></td><td>doc comments</td><td><code>xcode.syntax.comment.doc</code>, <code>xcode.syntax.comment.doc.keyword</code>, <code>xcode.syntax.markup.code</code></td></tr>
      <tr><td><code>color11</code></td><td>constants</td><td><code>xcode.syntax.identifier.constant</code></td></tr>
      <tr><td><code>color12</code></td><td>URLs</td><td><code>xcode.syntax.url</code></td></tr>
      <tr><td><code>color13</code></td><td>preprocessor, macros, project</td><td><code>xcode.syntax.preprocessor</code>, <code>xcode.syntax.identifier.macro</code>, <code>xcode.syntax.project</code></td></tr>
      <tr><td><code>color14</code></td><td>system classes</td><td><code>xcode.syntax.identifier.class.system</code></td></tr>
      <tr><td><code>color15</code></td><td>--</td><td>--</td></tr>
    </tbody>
  </table>
</div>

<p>
  <code>color0</code>, <code>color8</code>, and <code>color15</code>
  are unused by the generator.
</p>

<p>
  Palette color values are used directly without blending or interpolation.
  Background-derived properties (current line highlight, selection color,
  insertion point) are computed automatically based on background luminance.
</p>

<p><a href="../../README.md">Back to root README</a></p>
