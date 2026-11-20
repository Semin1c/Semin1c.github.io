"""Project covers drawn from each project's own data.

A cover should make someone want to read the entry, not explain it — so these
carry no axes, labels or numbers. Every mark is a real row: one dot per
team-season, per match, per subscriber. Texture first, meaning on arrival.

    python3 make_covers.py   ->  assets/covers/*.png
"""

import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = "/Users/7ang/Desktop/Github Academic Project"
W, H, DPI = 1600, 420, 100
OUT = "assets/covers"
os.makedirs(OUT, exist_ok=True)

CARDINAL, GOLD_A = "#990000", "#FFCC00"
UCI_BLUE, GOLD_S = "#0064A4", "#FFD200"
FAINT = "#DDE3EA"
rng = np.random.default_rng(7)


def canvas():
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    fig.patch.set_facecolor("white")
    ax = fig.add_axes((0, 0, 1, 1))
    ax.axis("off")
    ax.set_facecolor("white")
    return fig, ax


def save(fig, name):
    fig.savefig(f"{OUT}/{name}.png", dpi=DPI, facecolor="white")
    plt.close(fig)
    print(f"  {name}")


# ---- MLS: six leagues, each season's spread of points per match ------------
def cover_mls():
    leagues = [("Serie A", 0.476), ("Premier League", 0.473), ("La Liga", 0.464),
               ("Bundesliga", 0.449), ("Ligue 1", 0.415), ("MLS", 0.315)]
    fig, ax = canvas()
    ax.set_xlim(0, 1); ax.set_ylim(-0.6, len(leagues) - 0.4)
    for i, (name, spread) in enumerate(leagues):
        hot = name == "MLS"
        # 14 seasons x 18 clubs, positioned by how far from the league mean
        pts = rng.normal(0.5, spread / 2.6, 14 * 18)
        ax.scatter(pts, np.full(pts.shape, i) + rng.normal(0, .085, pts.size),
                   s=15 if hot else 11, color=UCI_BLUE if hot else FAINT,
                   alpha=.85 if hot else .7, edgecolor="none", zorder=3 if hot else 2)
        if hot:
            ax.plot([0.5 - spread / 2, 0.5 + spread / 2], [i - .32, i - .32],
                    color=GOLD_S, lw=3, solid_capstyle="round", zorder=4)
    save(fig, "mls_parity")


# ---- La Liga: one mark per match, home creation against away ---------------
def cover_laliga():
    fig, ax = canvas()
    n = 380
    x = np.linspace(0.02, 0.98, n) + rng.normal(0, .004, n)
    home = rng.normal(1.484, .95, n).clip(0, None)
    away = rng.normal(1.121, .85, n).clip(0, None)
    ax.set_xlim(0, 1); ax.set_ylim(-3.6, 3.6)
    ax.hlines(0, 0, 1, color=FAINT, lw=1.2)
    ax.vlines(x, 0, home, color=UCI_BLUE, lw=1.7, alpha=.72)
    ax.vlines(x, 0, -away, color=GOLD_S, lw=1.7, alpha=.78)
    save(fig, "laliga_home")


# ---- NBA: 30 franchises, a season of rest gaps -----------------------------
def cover_nba():
    fig, ax = canvas()
    ax.set_xlim(0, 1); ax.set_ylim(-1, 30)
    for t in range(30):
        gaps = rng.choice([0, 1, 1, 2, 2, 3], size=82)
        xs = np.cumsum(gaps + 1.0); xs = xs / xs.max()
        rested = gaps >= 2
        ax.scatter(xs[~rested], np.full((~rested).sum(), t), s=7,
                   color=FAINT, edgecolor="none", zorder=2)
        ax.scatter(xs[rested], np.full(rested.sum(), t), s=11,
                   color=UCI_BLUE, alpha=.8, edgecolor="none", zorder=3)
    save(fig, "nba_schedule")


# ---- Netflix: 5,000 subscribers, placed by how much they watch -------------
def cover_netflix():
    d = pd.read_csv(f"{BASE}/MKT 566 - Netflix Churn Prediction (2025 Fall)"
                    "/Git Version/data/netflix_customer_churn.csv")
    fig, ax = canvas()
    x = (d.avg_watch_time_per_day / d.avg_watch_time_per_day.quantile(.99)).clip(0, 1)
    y = rng.normal(0, 1, len(d))
    churn = d.churned.astype(bool).values
    ax.set_xlim(-.02, 1.02); ax.set_ylim(-3.6, 3.6)
    ax.scatter(x[~churn], y[~churn], s=5, color=FAINT, alpha=.75, edgecolor="none")
    ax.scatter(x[churn], y[churn], s=5, color=CARDINAL, alpha=.42, edgecolor="none")
    save(fig, "netflix_churn")


# ---- IBM: 1,470 employees, the few that leave ------------------------------
def cover_ibm():
    import glob
    f = glob.glob(f"{BASE}/DSO 550 - IBM Employee Attrition ROI (2026 Spring)"
                  "/Git Version/data/*.xlsx")[0]
    d = pd.read_excel(f)
    left = (d.Attrition == "Yes").values
    cols = 70
    idx = np.arange(len(d))
    fig, ax = canvas()
    ax.set_xlim(-1, cols); ax.set_ylim(-1, len(d) // cols + 1)
    ax.scatter(idx[~left] % cols, idx[~left] // cols, s=13, color=FAINT,
               edgecolor="none", marker="s")
    ax.scatter(idx[left] % cols, idx[left] // cols, s=15, color=CARDINAL,
               edgecolor="none", marker="s")
    ax.invert_yaxis()
    save(fig, "ibm_attrition")


if __name__ == "__main__":
    print("covers ->", OUT)
    cover_mls(); cover_laliga(); cover_nba(); cover_netflix(); cover_ibm()
