"""Scale scoring utilities."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import pandas as pd


def score_scale(data: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Calculate domain and total scores based on a configuration dictionary."""
    result = data.copy()

    domains = config.get("domains", {})
    for domain_name, items in domains.items():
        missing = [item for item in items if item not in result.columns]
        if missing:
            raise ValueError(f"Missing item columns for {domain_name}: {missing}")
        result[f"{domain_name}_score"] = result[items].sum(axis=1, skipna=False)

    total_items = config.get("total_items")
    if total_items:
        missing = [item for item in total_items if item not in result.columns]
        if missing:
            raise ValueError(f"Missing total item columns: {missing}")
        result["total_score"] = result[total_items].sum(axis=1, skipna=False)

    return result


def main() -> None:
    parser = argparse.ArgumentParser(description="Score scale data from a CSV file.")
    parser.add_argument("--data", required=True, help="Path to the input CSV file.")
    parser.add_argument("--config", required=True, help="Path to the JSON scoring configuration.")
    parser.add_argument("--output", required=True, help="Path to save the scored CSV file.")
    args = parser.parse_args()

    data = pd.read_csv(args.data)
    with open(args.config, "r", encoding="utf-8") as f:
        config = json.load(f)

    scored = score_scale(data, config)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    scored.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
