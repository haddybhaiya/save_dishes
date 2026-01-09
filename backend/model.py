# backend/model.py
import joblib
import pandas as pd
from pathlib import Path

from ml.preprocess import preprocess

MODEL_PATH = Path("ml/artifacts/model.pkl")

# Load model once 
model = joblib.load(MODEL_PATH)


def predict_waste(input_data: dict) -> float:
    """
    Predict food waste from input features
    """
    df = pd.DataFrame([input_data])

    # Preprocess for inference
    X = preprocess(df, training=False)

    prediction = model.predict(X)[0]
    return round(float(prediction), 2)
