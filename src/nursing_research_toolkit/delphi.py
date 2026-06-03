"""Delphi expert consultation summary utilities."""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def summarise_delphi(data: pd.DataFrame, rating_columns: list[str] | None = None) -> pd.DataFrame:
    """Summarise item-level Delphi ratings.

    I-CVI is calculated as the proportion of experts who rated an item as 4 or 5,
    assuming a 1-5 relevance scale.
    """
    if rating_columns is None:
        rating_columns = [col for col in data.columns if col.lower().startswith("item")]

    rows = []
    for col in rating_columns:
        values = pd.to_numeric(data[col], errors="coerce").dropna()
        if values.empty:
            continue

        mean = values.mean()
        sd = values.std(ddof=1) if len(values) > 1 else np.nan
        cv = sd / mean if mean != 0 and not np.isnan(sd) else np.nan

        rows.append(
            {
                "item": col,
                "n_experts": int(values.shape[0]),
                "mean": round(mean, 3),
                "sd": round(sd, 3) if not np.isnan(sd) else np.nan,
                "coefficient_of_variation": round(cv, 3) if not np.isnan(cv) else np.nan,
                "median": round(values.median(), 3),
                "iqr": round(values.quantile(0.75) - values.quantile(0.25), 3),
                "i_cvi": round((values >= 4).mean(), 3),
            }
        )

    return pd.DataFrame(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarise Delphi expert ratings.")
    parser.add_argument("--data", required=True, help="Path to the Delphi rating CSV file.")
    parser.add_argument("--output", required=True, help="Path to save the summary CSV file.")
    args = parser.parse_args()

    data = pd.read_csv(args.data)
    summary = summarise_delphi(data)
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(args.output, index=False)


if __name__ == "__main__":
    main()
