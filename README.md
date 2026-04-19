# ML Marks Predictor API

A machine learning project that predicts student marks based on study hours.

---

## Features

* Predict student marks using Linear Regression
* REST API built with FastAPI
* Simple and lightweight ML model

---

## Tech Stack

* Python
* scikit-learn
* FastAPI
* NumPy

---

##  How to Run

```bash id="run123"
pip install fastapi uvicorn scikit-learn numpy
uvicorn main:app --reload
```

---

## API Endpoint

* `/predict?hours=5`

Example response:

```json id="json123"
{
  "hours_studied": 5,
  "predicted_marks": 50
}
```

---

##  What I Learned

* Machine Learning basics
* Model training
* API integration
* End-to-end AI system design
