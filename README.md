<img width="1705" height="293" alt="image" src="https://github.com/user-attachments/assets/3547f4e7-efda-416a-a5b9-e9eab58b3825" />

### SaveDishes is an end-to-end machine learning application designed to help restaurants **predict daily food waste** and make **data-driven kitchen decisions** to reduce cost and environmental impact.

---

## 🌐 Live Links (Copy-Paste Friendly)
- Frontend: https://savedishes.streamlit.com </br>
- API: https://save-dishes-api.onrender.com  (run this first) </br>
- Docs: https://save-dishes-api.onrender.com/docs</br>

⚠️ Note: First request may take ~30 seconds due to free-tier cold start.

---

## 🚨 Problem Statement

Food waste is a major operational and environmental challenge for restaurants.  
Overproduction due to inaccurate demand estimation leads to:

- Financial losses  
- Inefficient resource utilization  
- Increased environmental impact  

Most small and mid-sized restaurants rely on intuition rather than data-driven planning.

---

## 🧠 Machine Learning Details

- **Model:** Random Forest Regressor  
- **Framework:** scikit-learn  

### Preprocessing Pipeline
- Date feature extraction (month, day, weekend)
- One-hot encoding of categorical features
- Feature consistency enforced using saved schema

### Evaluation Metrics
- Mean Absolute Error (MAE)
- R² Score

---

## 🧰 Tech Stack

### Machine Learning
- Python
- pandas
- scikit-learn

### Backend
- FastAPI
- Docker
- Render

### Frontend
- Streamlit
- Streamlit Community Cloud

### Tooling
- Git & GitHub
- Dockerized services
- Auto-deploy via GitHub integration

---

## ▶️ Run Locally

### 1️. Clone the Repository
```bash
git clone https://github.com/<your-username>/save-dishes.git
cd save-dishes
```
### 2️. Backend (FastAPI)
Install dependencies
```
pip install -r requirements.txt
```
Run API server
```
uvicorn app:app --host 0.0.0.0 --port 8000
```
Test API
```
http://localhost:8000/docs
```
### 3️. Frontend (Streamlit)
```
streamlit run app.py
```
Streamlit app will open at:
```
http://localhost:8501
```
---
##  📌 Key Highlights

- End-to-end ML pipeline<br>
- Feature consistency between training and inference<br>
- Dockerized backend<br>
- Cloud-hosted frontend & backend<br>
- Designed as a real-world decision-support system<br>

---
## 📁 Project Structure
```
save_dishes/
│
├── ml/
|   ├── model.ipynb
│   ├── preprocess.py
│   ├── train.py
|   ├── test.py
│   └── artifacts/
│       ├── model.pkl
│       └── feature_columns.pkl
│
├── backend/
|   ├── __init__.py
|   ├── requirements.txt
|   ├── readme.md
│   ├── app.py
│   ├── model.py
│   └── schemas.py
│
├── frontend/
|   ├── requirements.txt
│   ├── app.py
│   └── Dockerfile
│
├── DockerFile
├── .gitignore
└── README.md
```
---
## 🔄 How the System Works
- Historical data is preprocessed and used to train the ML model.
- The trained model and feature schema are saved as artifacts.
- FastAPI loads the model once and exposes a /predict endpoint.
- Streamlit frontend collects user input and sends it to the backend.
- The backend returns a food waste prediction.
- The frontend displays the result with business-friendly insights.
---

# 👨‍💻 Author : haddybhaiya ;)



