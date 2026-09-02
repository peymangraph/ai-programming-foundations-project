"""Reusable cleaning functions for the synthetic maintenance workflow."""

from __future__ import annotations

import numpy as np
import pandas as pd

CANONICAL_ASSET_TYPES = {
    "hvac": "HVAC",
    "electrical": "Electrical",
    "plumbing": "Plumbing",
    "elevator": "Elevator",
    "fire/life safety": "Fire/Life Safety",
    "lighting": "Lighting",
    "pump": "Pump",
    "appliance": "Appliance",
    "access control": "Access Control",
    "building envelope": "Building Envelope",
}

CANONICAL_PRIORITIES = {
    "low": "Low",
    "medium": "Medium",
    "high": "High",
    "emergency": "Emergency",
}


def standardize_categories(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with canonical asset-type and priority labels."""
    cleaned = df.copy()
    asset_key = cleaned["asset_type"].astype("string").str.strip().str.lower()
    priority_key = cleaned["priority"].astype("string").str.strip().str.lower()
    cleaned["asset_type"] = asset_key.map(CANONICAL_ASSET_TYPES).fillna(
        cleaned["asset_type"].astype("string").str.strip()
    )
    cleaned["priority"] = priority_key.map(CANONICAL_PRIORITIES).fillna(
        cleaned["priority"].astype("string").str.strip()
    )
    return cleaned


def remove_duplicate_work_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with duplicate work-order IDs removed."""
    return df.drop_duplicates(subset="work_order_id", keep="first").reset_index(drop=True).copy()


def flag_invalid_values(df: pd.DataFrame) -> pd.DataFrame:
    """Replace documented impossible or injected out-of-range values with NaN."""
    cleaned = df.copy()
    invalid_age = (cleaned["asset_age_years"] < 0) | (cleaned["asset_age_years"] > 50)
    invalid_resolution = (cleaned["resolution_hours"] <= 0) | (cleaned["resolution_hours"] > 240)
    invalid_cost = (cleaned["estimated_repair_cost"] < 0) | (cleaned["estimated_repair_cost"] > 25000)
    cleaned.loc[invalid_age, "asset_age_years"] = np.nan
    cleaned.loc[invalid_resolution, "resolution_hours"] = np.nan
    cleaned.loc[invalid_cost, "estimated_repair_cost"] = np.nan
    return cleaned


def impute_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill selected missing values while preserving all work-order rows."""
    cleaned = df.copy()
    cleaned["asset_condition"] = cleaned["asset_condition"].fillna("Unknown")
    numeric_columns = [
        "asset_age_years",
        "days_since_last_service",
        "estimated_repair_cost",
        "resolution_hours",
    ]
    group_columns = ["asset_type", "maintenance_type"]
    for column in numeric_columns:
        group_median = cleaned.groupby(group_columns, dropna=False)[column].transform("median")
        cleaned[column] = cleaned[column].fillna(group_median)
        cleaned[column] = cleaned[column].fillna(cleaned[column].median())
    return cleaned
