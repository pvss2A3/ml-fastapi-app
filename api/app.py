from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()
model = joblib.load("model/diabetes_model.pkl")

class DiabetesFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Diabetes Prediction API"}

@app.post("/predict")
def predict(features: DiabetesFeatures):
    input_df = pd.DataFrame([features.dict()])
    prediction = model.predict(input_df)[0]
    return {"prediction": prediction}

