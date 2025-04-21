import os            # For checking file paths
import joblib        # For loading the saved model
import pandas as pd  # For reading the dataset
import numpy as np   # For checking prediction output type

# Test 1: Check that the model file exists at the given path
def test_model_file_exists():
    """Check if the XGBoost .pkl file exists."""
    assert os.path.exists("../models/xgboost_model.pkl"), "Model file not found."
# Test 2: Try to load the model from the .pkl file
def test_load_model():
    """Check that the XGBoost model loads correctly."""
    model = joblib.load("../models/xgboost_model.pkl")
    assert model is not None, "Failed to load XGBoost model."
# Test 3: Ensure the model can make valid predictions on the input features
def test_model_prediction():
    """Test if the XGBoost model can make predictions."""
    df = pd.read_csv("../data/processed/cleaned_data.csv")  # Load the processed dataset
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]] # Extract the input features from the DataFrame
    # Load the saved model
    model = joblib.load("../models/xgboost_model.pkl")
    y_pred = model.predict(X) # Make predictions using the model

    assert len(y_pred) == len(X), "Prediction length mismatch." # Check if the number of predictions matches the number of input rows
    assert isinstance(y_pred, (np.ndarray, list)), "Prediction output is not array or list." # Check that the output is either a NumPy array or a list
