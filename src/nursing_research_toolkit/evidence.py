"""Evidence-synthesis screening log utilities."""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def summarise_screening(data: pd.DataFrame) -> pd.DataFrame:
    """Summarise include/exclude decisions and exclusion reasons."""
    required = {"decision"}
    missing = required - set(data.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    decision_summary = (
        data["decision"]
        .fillna("missing")
        .value_counts()
        .rename_axis("category")
        .reset_index(name="count")
    )
    decision_summary.insert(0, "section", "decision")

    if "reason" in data.columns:
        decision_lower = data["decision"].fillna("").astype(str).str.lower()
        reason_summary = (
            data.loc[decision_lower.eq("exclude"), "reason"]
            .fillna("not_reported")
            .replace("", "not_reported")
            .value_counts()
            .rename_axis("category")
            .reset_index(name="count")
        )
        reason_summary.insert(0, "section", "exclusion_reason")
        return pd.concat([decision_summary, reason_summary], ignore_index=True)

    return decision_summary


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise an evidence-synthesis screening log.")
    parser.add_argument("--data", required=True, help="Path to the screening log CSV file.")
    parser.add_argument("--output", required=True, help="Path to save the summary CSV file.")
    args = parser.parse_args()

    data = pd.read_csv(args.data)
    summary = summarise_screening(data)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
