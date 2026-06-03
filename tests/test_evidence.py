import pandas as pd

from nursing_research_toolkit.evidence import summarise_screening


def test_summarise_screening_decisions():
    data = pd.DataFrame(
        {
            "decision": ["include", "exclude", "exclude"],
            "reason": ["", "wrong population", "wrong intervention"],
        }
    )

    summary = summarise_screening(data)

    assert "decision" in summary["section"].tolist()
    assert "exclusion_reason" in summary["section"].tolist()
