# backend/app.py

from fastapi import FastAPI
from backend.schemas import PredictionInput, PredictionOutput
from backend.model import predict_waste

app = FastAPI(
    title="Food Waste Prediction API",
    description="Predict daily food waste for restaurants",
    version="1.0.0"
)


@app.get("/")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    prediction = predict_waste(input_data.dict())
    return {"predicted_food_waste_kg": prediction}
