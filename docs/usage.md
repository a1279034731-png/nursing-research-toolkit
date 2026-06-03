# Usage guide

## Scale scoring

Prepare a CSV file where each row is a participant and each item is stored in a column. Define item groups in a JSON configuration file.

Example:

```json
{
  "domains": {
    "clinical_control": ["item_1", "item_2", "item_3"],
    "professional_meaning": ["item_4", "item_5"]
  },
  "total_items": ["item_1", "item_2", "item_3", "item_4", "item_5"]
}
```

Run:

```bash
python -m nursing_research_toolkit.scale_scoring --data examples/sample_scale_data.csv --config examples/scale_config.json --output scored.csv
```

## Delphi summary

Prepare a CSV file where each row is an expert and each item rating is stored in a column. The current implementation assumes a 1-5 relevance rating and calculates I-CVI as the proportion of experts rating the item as 4 or 5.

Run:

```bash
python -m nursing_research_toolkit.delphi --data examples/sample_delphi_panel.csv --output delphi_summary.csv
```

## Evidence screening summary

Prepare a CSV screening log with columns such as `record_id`, `decision`, and `reason`.

Run:

```bash
python -m nursing_research_toolkit.evidence --data examples/sample_screening_log.csv --output screening_summary.csv
```
