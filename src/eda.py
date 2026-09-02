"""Reusable exploratory-analysis helpers for maintenance work-order data."""

from __future__ import annotations

import pandas as pd

PRIORITY_ORDER = ["Low", "Medium", "High", "Emergency"]


def priority_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return work-order counts and percentages for each priority level."""
    counts = df["priority"].value_counts().reindex(PRIORITY_ORDER, fill_value=0)
    percentages = (
        df["priority"].value_counts(normalize=True)
        .reindex(PRIORITY_ORDER, fill_value=0)
        .mul(100)
        .round(2)
    )
    return pd.DataFrame({"count": counts, "percentage": percentages})


def asset_type_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Summarize work-order volume, failures, cost, and resolution by asset type."""
    return (
        df.groupby("asset_type")
        .agg(
            work_orders=("work_order_id", "count"),
            avg_asset_age_years=("asset_age_years", "mean"),
            avg_previous_failures=("previous_failures_12m", "mean"),
            median_repair_cost=("estimated_repair_cost", "median"),
            median_resolution_hours=("resolution_hours", "median"),
        )
        .round(2)
        .sort_values("work_orders", ascending=False)
    )
