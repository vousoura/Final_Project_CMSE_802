import os  # For creating directories and handling file paths
import joblib  # For saving the trained model to a file
import pandas as pd  # For data handling and manipulation
import numpy as np  # For numerical operations, especially for computing RMSE
from sklearn.ensemble import RandomForestRegressor  # Machine learning model
from sklearn.model_selection import train_test_split  # For splitting the dataset
from sklearn.metrics import mean_squared_error  # For evaluating the model performance
import matplotlib.pyplot as plt  # For plotting
import seaborn as sns  # For prettier plots

# Function to load the dataset from a CSV file
def load_data(filepath="../data/processed/cleaned_data.csv"):
    return pd.read_csv(filepath)
# Function to train a Random Forest model and return the model, RMSE, and predictions
def random_forest_regression(X_train, X_test, y_train, y_test):
    model = RandomForestRegressor(n_estimators=100, random_state=42)  # Create the RF model
    model.fit(X_train, y_train)  # Train the model
    y_pred = model.predict(X_test)  # Predict on the test set
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))  # Calculate RMSE
    return model, rmse, y_pred  # Return the trained model, RMSE, and predictions

# Main function
def main():
    df = load_data()  # Load the cleaned dataset
    # Select feature columns and target column
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]]
    y = df["Velocity"]
    # Split the data into training and testing sets (75/25 split)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    # Train the model and get predictions
    rf_model, rf_rmse, y_pred = random_forest_regression(X_train, X_test, y_train, y_test)
    # Create directories if they don't exist
    os.makedirs("../models", exist_ok=True)
    os.makedirs("../results", exist_ok=True)
    # Save the trained model using joblib
    joblib.dump(rf_model, "../models/random_forest_model.pkl")
    print("Random Forest model saved.")
    # Save the RMSE result to a text file
    with open("../results/random_forest_rmse.txt", "w") as f:
        f.write(str(rf_rmse))
    # Print RMSE 
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
# Entry point for the script
if __name__ == "__main__":
    main() # Run the main function
