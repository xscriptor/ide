import json
import os

PARENT = os.path.dirname(__file__)
DIST_DIR = os.path.join(PARENT, "themes")
os.makedirs(DIST_DIR, exist_ok=True)

with open(os.path.join(PARENT, "..", "..", "colors.json")) as f:
    palettes = json.load(f)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def blend(ha, hb, pct):
    ra, ga, ba = hex_to_rgb(ha)
    rb, gb, bb = hex_to_rgb(hb)
    return rgb_to_hex(
        round(ra + (rb - ra) * pct),
        round(ga + (gb - ga) * pct),
        round(ba + (bb - ba) * pct),
    )


def relative_luminance(r, g, b):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def contrast_ratio(ha, hb):
    r1, g1, b1 = hex_to_rgb(ha)
    r2, g2, b2 = hex_to_rgb(hb)
    l1 = relative_luminance(r1, g1, b1)
    l2 = relative_luminance(r2, g2, b2)
    return (max(l1, l2) + 0.05) / (min(l1, l2) + 0.05)


def accessible_comment(bg, fg, comment_candidate):
    if contrast_ratio(comment_candidate, bg) >= 3.0:
        return comment_candidate
    for pct in (0.15, 0.25, 0.35, 0.5, 0.65, 0.8):
        candidate = blend(bg, fg, pct)
        if contrast_ratio(candidate, bg) >= 3.0:
            return candidate
    return blend(bg, fg, 0.65)


def hex_to_bgr_win(h):
    h = h.lstrip("#")
    r, g, b = h[0:2], h[2:4], h[4:6]
    return "0x00" + f"{b}{g}{r}".upper()


VSSETTINGS_TEMPLATE = """\
<UserSettings>
  <ApplicationIdentity version="17.0"/>
  <ToolsOptions>
    <ToolsOptionsCategory name="Environment" RegisteredName="Environment">
      <Category name="FontsAndColors" Category="{{1EDA5DD4-927A-43A7-810E-7FD247D0DA11}}" Package="{{F5E7E717-1221-4B36-9B1C-5A85AD223A5F}}" RegisteredName="FontsAndColors" PackageName="Visual Studio Environment">
        <Property name="Version">2.0</Property>
        <Property name="ThemeName">Xscriptor {name}</Property>
        <Property name="IsDirty">true</Property>
        <Items>
          <Item Name="Plain Text" Background="{bg_win}" Foreground="{fg_win}"/>
          <Item Name="Selected Text" Background="{fg_at_15pct_win}"/>
          <Item Name="Inactive Selected Text" Background="{fg_at_08pct_win}"/>
          <Item Name="CurrentLine" Background="{blend_bg_fg_5pct_win}"/>
          <Item Name="Line Numbers" Foreground="{comment_color_win}"/>
          <Item Name="Comment" Foreground="{comment_color_win}"/>
          <Item Name="String" Foreground="{color2_win}"/>
          <Item Name="String (C# @ Verbatim)" Foreground="{color2_win}"/>
          <Item Name="Number" Foreground="{color3_win}"/>
          <Item Name="Keyword" Foreground="{color5_win}"/>
          <Item Name="Type" Foreground="{color6_win}"/>
          <Item Name="User Types" Foreground="{color6_win}"/>
          <Item Name="Identifier" Foreground="{fg_win}"/>
          <Item Name="Operator" Foreground="{color5_win}"/>
          <Item Name="Preprocessor Keyword" Foreground="{color9_win}"/>
          <Item Name="Excluded Code" Foreground="{comment_color_win}"/>
        </Items>
      </Category>
    </ToolsOptionsCategory>
  </ToolsOptions>
</UserSettings>"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]

    comment_color_hex = accessible_comment(bg, fg, c["color8"])

    def col(idx):
        return c[f"color{idx}"]

    vals = {
        "name": name,
        "bg_win": hex_to_bgr_win(bg),
        "fg_win": hex_to_bgr_win(fg),
        "fg_at_15pct_win": hex_to_bgr_win(blend(bg, fg, 0.15)),
        "fg_at_08pct_win": hex_to_bgr_win(blend(bg, fg, 0.08)),
        "blend_bg_fg_5pct_win": hex_to_bgr_win(blend(bg, fg, 0.05)),
        "comment_color_win": hex_to_bgr_win(comment_color_hex),
        "color2_win": hex_to_bgr_win(col(2)),
        "color3_win": hex_to_bgr_win(col(3)),
        "color4_win": hex_to_bgr_win(col(4)),
        "color5_win": hex_to_bgr_win(col(5)),
        "color6_win": hex_to_bgr_win(col(6)),
        "color9_win": hex_to_bgr_win(col(9)),
    }

    vssettings = VSSETTINGS_TEMPLATE.format(**vals)

    filepath = os.path.join(DIST_DIR, f"{name}.vssettings")
    with open(filepath, "w") as f:
        f.write(vssettings)
    print(f"  {name}.vssettings")

print("\nDone! Generated 12 Visual Studio .vssettings files.")
