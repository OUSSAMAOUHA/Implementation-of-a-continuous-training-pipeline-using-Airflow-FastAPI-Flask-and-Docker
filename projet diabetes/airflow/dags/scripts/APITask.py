import pickle
import uvicorn
from fastapi import FastAPI
import numpy as np  # Add this import

from pydantic import BaseModel


app = FastAPI()
import joblib

class Diabetes(BaseModel):
    Pregnancies:int
    Glucose:int
    BloodPressure:int
    SkinThickness:int
    Insulin:int
    BMI:float
    DPF:float
    Age:int
# Chargement du modèle
model_path = "/opt/airflow/dags/scripts/xgb_model.pkl"  # Mettez le chemin correct s'il est différent
model = joblib.load(open(model_path, "rb"))

@app.get("/")
def great():
    return {"message": "bonjour"}

@app.post("/predict")
def predict(req: Diabetes):
    preg = req.Pregnancies
    glucose = req.Glucose
    bp = req.BloodPressure
    skinthickness = req.SkinThickness
    insulin = req.Insulin
    bmi = req.BMI
    dpf = req.DPF
    age = req.Age
    features = np.array([preg, glucose, bp, skinthickness, insulin, bmi, dpf, age]).reshape(1, -1)  # Convert to NumPy array
    prediction = model.predict(features)[0]
    probab = model.predict_proba(features)

    if prediction == 1:
        return {"ans": f"You have been tested positive with {probab[0][1]} probability"}
    else:
        return {"ans": f"You have been tested negative with {probab[0][0]} probability"}

if __name__ == "__main__":
    uvicorn.run(app)