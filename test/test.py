import pandas as pd

def test_dataset_load():
    df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")
    assert not df.empty

def test_columns_exist():
    df = pd.read_csv("AI_Impact_on_Jobs_2030.csv")
    # change column names based on your dataset
    assert len(df.columns) > 0
``
