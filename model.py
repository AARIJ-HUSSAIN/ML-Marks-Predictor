import numpy as np
from sklearn.linear_model import LinearRegression

# Sample dataset (hours studied → marks)
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([20, 25, 35, 45, 50, 60, 70, 80])

# Train model
model = LinearRegression()
model.fit(X, y)

def predict_marks(hours):
    return model.predict([[hours]])[0]