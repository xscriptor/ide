import json
import os

PARENT = os.path.dirname(__file__)
THEMES_DIR = os.path.join(PARENT, "themes")
os.makedirs(THEMES_DIR, exist_ok=True)

with open(os.path.join(PARENT, "..", "..", "colors.json")) as f:
    palettes = json.load(f)


def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def rgba_str(h, a):
    r, g, b = hex_to_rgb(h)
    return f"rgba({r}, {g}, {b}, {a})"


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


TEMPLATE = """\
;;; xscriptor-{name_lower}-theme.el --- Xscriptor {name} theme

(deftheme xscriptor-{name_lower}
  "Xscriptor {name} theme")

(let ((class '((class color) (min-colors 89))))
  (custom-theme-set-faces
   'xscriptor-{name_lower}
   `(default ((,class (:background "{bg}" :foreground "{fg}"))))
   `(cursor ((,class (:background "{color5}"))))
   `(region ((,class (:background "{fg_at_15pct_rgba}"))))
   `(fringe ((,class (:background "{bg}"))))
   `(linum ((,class (:foreground "{comment_color}" :background "{bg}"))))
   `(line-number ((,class (:foreground "{comment_color}" :background "{bg}"))))
   `(line-number-current-line ((,class (:foreground "{color5}" :background "{blend_bg_fg_5pct}"))))
   `(mode-line ((,class (:background "{color0}" :foreground "{fg}"))))
   `(mode-line-inactive ((,class (:background "{color0}" :foreground "{comment_color}"))))
   `(minibuffer-prompt ((,class (:foreground "{color5}"))))
   `(font-lock-comment-face ((,class (:foreground "{comment_color}" :italic t))))
   `(font-lock-comment-delimiter-face ((,class (:foreground "{comment_color}" :italic t))))
   `(font-lock-string-face ((,class (:foreground "{color2}"))))
   `(font-lock-doc-face ((,class (:foreground "{color2}"))))
   `(font-lock-doc-markup-face ((,class (:foreground "{color2}"))))
   `(font-lock-keyword-face ((,class (:foreground "{color5}"))))
   `(font-lock-builtin-face ((,class (:foreground "{color6}"))))
   `(font-lock-function-name-face ((,class (:foreground "{color4}"))))
   `(font-lock-variable-name-face ((,class (:foreground "{fg}"))))
   `(font-lock-type-face ((,class (:foreground "{color6}"))))
   `(font-lock-constant-face ((,class (:foreground "{color3}"))))
   `(font-lock-warning-face ((,class (:foreground "{color3}"))))
   `(font-lock-preprocessor-face ((,class (:foreground "{color9}"))))
   `(font-lock-negation-char-face ((,class (:foreground "{color5}"))))
   `(font-lock-regexp-grouping-backslash ((,class (:foreground "{color1}"))))
   `(font-lock-regexp-grouping-construct ((,class (:foreground "{color1}"))))
   `(highlight ((,class (:background "{blend_bg_fg_5pct}"))))
   `(match ((,class (:background "{color3}" :foreground "{bg}"))))
   `(isearch ((,class (:background "{color3}" :foreground "{bg}"))))
   `(lazy-highlight ((,class (:background "{color3_30pct}"))))
   `(show-paren-match ((,class (:background "{color5}"))))
   `(show-paren-mismatch ((,class (:background "{color1}"))))
   `(link ((,class (:foreground "{color6}" :underline t))))
   `(button ((,class (:underline t :foreground "{color6}"))))
   `(success ((,class (:foreground "{color2}"))))
   `(warning ((,class (:foreground "{color3}"))))
   `(error ((,class (:foreground "{color1}"))))
   `(header-line ((,class (:background "{blend_bg_fg_5pct}" :foreground "{fg}"))))
   `(trailing-whitespace ((,class (:background "{color1}"))))
   `(whitespace-space ((,class (:foreground "{comment_color}" :background "{bg}"))))
   `(whitespace-tab ((,class (:foreground "{comment_color}" :background "{bg}"))))
   `(whitespace-newline ((,class (:foreground "{comment_color}"))))
   `(whitespace-trailing ((,class (:background "{color1}"))))
   `(dired-directory ((,class (:foreground "{color6}"))))
   `(dired-header ((,class (:foreground "{color4}"))))
   `(dired-marked ((,class (:foreground "{color5}"))))
   `(diff-added ((,class (:foreground "{color2}"))))
   `(diff-changed ((,class (:foreground "{color3}"))))
   `(diff-removed ((,class (:foreground "{color1}"))))
   `(diff-refine-added ((,class (:foreground "{color2}" :background "{bg}"))))
   `(diff-refine-changed ((,class (:foreground "{color3}" :background "{bg}"))))
   `(diff-refine-removed ((,class (:foreground "{color1}" :background "{bg}"))))
   `(magit-section-highlight ((,class (:background "{blend_bg_fg_5pct}"))))
   `(magit-diff-added ((,class (:foreground "{color2}"))))
   `(magit-diff-removed ((,class (:foreground "{color1}"))))
   ))

(provide-theme 'xscriptor-{name_lower})
;;; xscriptor-{name_lower}-theme.el ends here
"""


for name, c in palettes.items():
    bg = c["background"]
    fg = c["foreground"]
    name_lower = name.lower()

    comment_color = accessible_comment(bg, fg, c["color8"])
    blend_bg_fg_5pct = blend(bg, fg, 0.05)

    def col(idx):
        return c[f"color{idx}"]

    content = TEMPLATE.format(
        name=name,
        name_lower=name_lower,
        bg=bg,
        fg=fg,
        comment_color=comment_color,
        color0=col(0),
        color1=col(1),
        color2=col(2),
        color3=col(3),
        color4=col(4),
        color5=col(5),
        color6=col(6),
        color9=col(9),
        blend_bg_fg_5pct=blend_bg_fg_5pct,
        fg_at_15pct_rgba=rgba_str(fg, 0.15),
        color3_30pct=rgba_str(col(3), 0.3),
    )

    filename = f"xscriptor-{name_lower}-theme.el"
    filepath = os.path.join(THEMES_DIR, filename)
    with open(filepath, "w") as f:
        f.write(content.lstrip())
    print(f"  \u2713 {filename}")

print("\nDone! Generated 12 Emacs color themes.")
