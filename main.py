from fastapi import FastAPI
from model import predict_marks

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ML Marks Predictor API"}

@app.get("/predict")
def predict(hours: float):
    result = predict_marks(hours)
    return {
        "hours_studied": hours,
        "predicted_marks": result
    }