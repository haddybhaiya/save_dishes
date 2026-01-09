# backend/schemas.py

from pydantic import BaseModel


class PredictionInput(BaseModel):
    staff_experience: str
    waste_category: str
    day_of_week: int
    date: str
    temperature: float
    total_sales: float


class PredictionOutput(BaseModel):
    predicted_food_waste_kg: float
