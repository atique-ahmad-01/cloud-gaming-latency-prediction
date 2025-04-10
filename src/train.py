from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

import joblib
import os

def train_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }

    trained_models = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        trained_models[name] = model
        # ✅ Save model to models/ folder
        filename = f"models/{name.replace(' ', '_').lower()}_model.pkl"
        os.makedirs("models", exist_ok=True)
        joblib.dump(model, filename)
        print(f"Saved {name} to {filename}")

    return trained_models, X_test, y_test
