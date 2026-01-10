# backend/schemas.py

from pydantic import BaseModel


class PredictionInput(BaseModel):
    staff_experience: str
    waste_category: str
    day_of_week: int
    date: str
    temperature_C: float
    humidity_percent: float
    kitchen_staff: int
    meals_served: int
    past_waste_kg: float
    special_event: int 
    


class PredictionOutput(BaseModel):
    predicted_food_waste_kg: float
