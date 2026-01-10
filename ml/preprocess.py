# ml/preprocess.py
import pandas as pd
import joblib
from pathlib import Path

FEATURE_PATH = Path("ml/artifacts/feature_columns.pkl")

def preprocess(df: pd.DataFrame, training=True):
    df = df.copy()

    # target
    y = None
    if training:
        y = df["food_waste_kg"].values
        df = df.drop(columns=["food_waste_kg"])

    # date features
    df["date"] = pd.to_datetime(df["date"])
    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["is_weekend"] = (df["day_of_week"] >= 5).astype(int)
    df.drop(columns=["date"], inplace=True)

    # one-hot encoding
    df = pd.get_dummies(
        df,
        columns=["staff_experience", "waste_category"],
        drop_first=True
    )

    if training:
        # save feature space
        FEATURE_PATH.parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(df.columns.tolist(), FEATURE_PATH)
        return df, y
    else:
        # load feature space & align
        feature_cols = joblib.load(FEATURE_PATH)
        df = df.reindex(columns=feature_cols, fill_value=0)
        return df
