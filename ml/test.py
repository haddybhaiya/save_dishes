# ml/evaluate.py
import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from preprocess import preprocess
df = pd.read_csv("train.csv")
X, y = preprocess(df, training=True)
model = joblib.load("artifacts/model.pkl")
preds = model.predict(X)
mae = mean_absolute_error(y, preds)
rmse = mean_squared_error(y, preds, squared=False)
r2 = r2_score(y, preds)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")
