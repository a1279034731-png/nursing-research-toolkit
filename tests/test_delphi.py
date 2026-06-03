import pandas as pd

from nursing_research_toolkit.delphi import summarise_delphi


def test_summarise_delphi_i_cvi():
    data = pd.DataFrame({"item_1": [5, 4, 3, 4]})

    summary = summarise_delphi(data)

    assert summary.loc[0, "item"] == "item_1"
    assert summary.loc[0, "i_cvi"] == 0.75
