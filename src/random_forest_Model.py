import os
import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(filepath="../data/processed/cleaned_data.csv"):
    return pd.read_csv(filepath)

def random_forest_regression(X_train, X_test, y_train, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    return model, rmse, y_pred

def main():
    df = load_data()
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]]
    y = df["Velocity"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    rf_model, rf_rmse, y_pred = random_forest_regression(X_train, X_test, y_train, y_test)

    os.makedirs("../models", exist_ok=True)
    os.makedirs("../results", exist_ok=True)

    joblib.dump(rf_model, "../models/random_forest_model.pkl")
    print("Random Forest model saved.")

    with open("../results/random_forest_rmse.txt", "w") as f:
        f.write(str(rf_rmse))

    print(f"Random Forest RMSE: {rf_rmse}")
    
    # Scatter plot: Actual vs Predicted Values
    plt.figure(figsize=(7, 5))
    sns.scatterplot(x=y_test, y=y_pred, color="green")
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], '--', color='red')
    plt.xlabel("Actual Velocity (m/s)")
    plt.ylabel("Predicted Velocity (m/s)")
    plt.title("Random Forest: Actual vs Predicted")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()