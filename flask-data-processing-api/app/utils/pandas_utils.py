import pandas as pd

def process_csv(file):
    df = pd.read_csv(file)

    df = df.dropna()
    df["value"] = df["value"].astype(float)

    grouped = (
        df.groupby("category")
        .agg(total_value=("value", "sum"),
             average_value=("value", "mean"))
        .reset_index()
    )

    return grouped
