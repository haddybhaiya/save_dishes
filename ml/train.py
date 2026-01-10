# ml/train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error , r2_score
import joblib

from preprocess import preprocess

# Load data
df = pd.read_csv("data/train.csv")

# Preprocess
X, y = preprocess(df, training=True)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
print("MAE:", mean_absolute_error(y_test, preds))
print("R2 Score:", r2_score(y_test, preds))

# Save model
import os


ARTIFACT_DIR = "ml/artifacts"
os.makedirs(ARTIFACT_DIR, exist_ok=True)

model_path = os.path.join(ARTIFACT_DIR, "model.pkl")
joblib.dump(model, model_path)

print(f"Model saved at {model_path}")

