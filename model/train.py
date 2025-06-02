import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
import joblib

def train_and_save_model():
    diabetes = load_diabetes()
    X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    y = pd.Series(diabetes.target)

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "model/diabetes_model.pkl")
    print("Model saved!")

if __name__ == "__main__":
    train_and_save_model()

