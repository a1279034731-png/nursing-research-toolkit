import pandas as pd

from nursing_research_toolkit.scale_scoring import score_scale


def test_score_scale_total_and_domains():
    data = pd.DataFrame(
        {
            "item_1": [1, 2],
            "item_2": [3, 4],
            "item_3": [5, 6],
        }
    )
    config = {
        "domains": {"domain_a": ["item_1", "item_2"]},
        "total_items": ["item_1", "item_2", "item_3"],
    }

    scored = score_scale(data, config)

    assert scored["domain_a_score"].tolist() == [4, 6]
    assert scored["total_score"].tolist() == [9, 12]
