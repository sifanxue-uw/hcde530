from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT.parent / "Week 4" / "seattle_bikes.csv"
CHART_DIR = ROOT / "charts"
CHART_DIR.mkdir(parents=True, exist_ok=True)


def prepare_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH)
    df["date"] = pd.to_datetime(df["date"])
    df["hour"] = df["date"].dt.hour
    df["dayofweek"] = df["date"].dt.dayofweek  # Monday=0 ... Sunday=6
    df["is_weekend"] = df["dayofweek"] >= 5
    df["total"] = df["fremont_bridge_nb"] + df["fremont_bridge_sb"]
    return df


def chart_q1_weekday_commute_pattern(df: pd.DataFrame) -> None:
    weekday = (
        df[~df["is_weekend"]]
        .groupby("hour", as_index=False)[["fremont_bridge_nb", "fremont_bridge_sb", "total"]]
        .mean()
    )

    plt.figure(figsize=(11, 6.5))
    plt.plot(weekday["hour"], weekday["fremont_bridge_nb"], marker="o", label="Northbound")
    plt.plot(weekday["hour"], weekday["fremont_bridge_sb"], marker="o", label="Southbound")
    plt.plot(weekday["hour"], weekday["total"], linestyle="--", label="Total")
    plt.title("Weekday Hourly Bike Counts at Fremont Bridge (Average per Hour)")
    plt.xlabel("Hour of Day (0-23)")
    plt.ylabel("Average Bike Count")
    plt.xticks(range(24))
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_DIR / "q1_weekday_commute_pattern.png", dpi=150)
    plt.close()


def chart_q3_weekend_pattern(df: pd.DataFrame) -> None:
    weekend = (
        df[df["is_weekend"]]
        .groupby("hour", as_index=False)[["fremont_bridge_nb", "fremont_bridge_sb", "total"]]
        .mean()
    )

    plt.figure(figsize=(11, 6.5))
    plt.plot(weekend["hour"], weekend["fremont_bridge_nb"], marker="o", label="Northbound")
    plt.plot(weekend["hour"], weekend["fremont_bridge_sb"], marker="o", label="Southbound")
    plt.plot(weekend["hour"], weekend["total"], linestyle="--", label="Total")
    plt.title("Weekend Hourly Bike Counts at Fremont Bridge (Average per Hour)")
    plt.xlabel("Hour of Day (0-23)")
    plt.ylabel("Average Bike Count")
    plt.xticks(range(24))
    plt.legend()
    plt.tight_layout()
    plt.savefig(CHART_DIR / "q3_weekend_pattern.png", dpi=150)
    plt.close()


def chart_q3_weekday_vs_weekend_total(df: pd.DataFrame) -> None:
    hourly = (
        df.groupby(["hour", "is_weekend"], as_index=False)["total"]
        .mean()
        .assign(day_type=lambda d: d["is_weekend"].map({False: "Weekday", True: "Weekend"}))
    )

    weekday = hourly[hourly["day_type"] == "Weekday"].set_index("hour")["total"]
    weekend = hourly[hourly["day_type"] == "Weekend"].set_index("hour")["total"]

    hours = list(range(24))
    weekday_vals = [weekday.get(h, 0) for h in hours]
    weekend_vals = [weekend.get(h, 0) for h in hours]

    x = range(24)
    width = 0.4

    plt.figure(figsize=(12, 6.5))
    plt.bar([i - width / 2 for i in x], weekday_vals, width=width, label="Weekday")
    plt.bar([i + width / 2 for i in x], weekend_vals, width=width, label="Weekend")
    plt.title("Weekday vs Weekend Hourly Total Bike Counts at Fremont Bridge")
    plt.xlabel("Hour of Day (0-23)")
    plt.ylabel("Average Bike Count")
    plt.xticks(hours)
    plt.legend(title="Day Type")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "q3_weekday_vs_weekend_total.png", dpi=150)
    plt.close()


def main() -> None:
    df = prepare_data()
    chart_q1_weekday_commute_pattern(df)
    chart_q3_weekend_pattern(df)
    chart_q3_weekday_vs_weekend_total(df)
    print(f"Saved charts to: {CHART_DIR}")


if __name__ == "__main__":
    main()
