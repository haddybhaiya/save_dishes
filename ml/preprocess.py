# ml/preprocess.py

import pandas as pd

def preprocess(df: pd.DataFrame, training: bool = True):
    df = df.copy()

    # 1. Clean categorical columns
    df['staff_experience'] = df['staff_experience'].fillna('unknown')
    df['staff_experience'] = df['staff_experience'].str.lower().str.strip()
    df['waste_category'] = df['waste_category'].str.lower().str.strip()

    # 2. Date features
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.month
    df['day'] = df['date'].dt.day

    df['is_weekend'] = df['day_of_week'].apply(
        lambda x: 1 if x >= 5 else 0
    )

    df.drop(columns=['date'], inplace=True)

    # 3. One-hot encoding
    df = pd.get_dummies(
        df,
        columns=['staff_experience', 'waste_category'],
        drop_first=True
    )

    # 4. Split target
    target_col = 'food_waste_kg'

    if training:
        y = df[target_col]
        X = df.drop(columns=[target_col, 'ID'])
        return X, y

    X = df.drop(columns=['ID'], errors='ignore')
    return X
