"""Social share cards — one per identity, 1200x630.

What a recruiter sees when the URL is pasted into LinkedIn, Slack or an email.
Run after changing names/roles in content.py:  python3 make_og.py
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from content import MODES, SHARED

W, H, DPI = 1200, 630, 100
INK, MUTED = "#0F172A", "#64748B"


def card(mode, path):
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor("white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.set_xlim(0, W); ax.set_ylim(0, H); ax.axis("off")

    # accent spine down the left, gold hairline beside it
    ax.add_patch(Rectangle((0, 0), 18, H, color=mode["accent"], zorder=2))
    ax.add_patch(Rectangle((18, 0), 5, H, color=mode["gold"], zorder=2))

    x = 86
    ax.text(x, H - 120, SHARED["name"], fontsize=62, fontweight="bold",
            color=INK, va="top", ha="left")
    ax.text(x, H - 205, mode["nav_tag"].replace("&amp;", "&"), fontsize=29,
            color=mode["accent"], va="top", ha="left", fontweight="semibold")
    ax.plot([x, x + 96], [H - 248, H - 248], color=mode["gold"], lw=5,
            solid_capstyle="butt")

    # three things he actually works on, straight from the About list
    for i, (label, _) in enumerate(mode["about_list"][:3]):
        y = H - 330 - i * 46
        ax.plot([x + 4], [y + 7], marker="s", markersize=7, color=mode["gold"])
        ax.text(x + 26, y, label, fontsize=23, color=INK, va="center", ha="left")

    blurb = ("Analyst roles from May 2026  ·  MS Business Analytics, USC Marshall")
    ax.text(x, 150, blurb, fontsize=21, color=MUTED, va="center", ha="left")
    ax.text(x, 92, "semin1c.github.io", fontsize=19, color=INK, va="center",
            ha="left", fontweight="semibold",
            path_effects=[pe.Normal()])

    fig.savefig(path, dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  wrote {path}")


if __name__ == "__main__":
    for key, mode in MODES.items():
        card(mode, f"assets/og_{key}.png")
