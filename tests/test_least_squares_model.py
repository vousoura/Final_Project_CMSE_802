import os
import joblib
import pandas as pd
import numpy as np

def test_model_file_exists():
    """Check if the Least Squares .pkl file exists."""
    assert os.path.exists("../models/least_squares_model.pkl"), "Model file not found."

def test_load_model():
    """Check that the Least Squares model loads correctly."""
    model = joblib.load("../models/least_squares_model.pkl")
    assert model is not None, "Failed to load Least Squares model."

def test_model_prediction():
    """Test if the Least Squares model can make predictions."""
    df = pd.read_csv("../data/processed/cleaned_data.csv")
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]]

    model = joblib.load("../models/least_squares_model.pkl")
    y_pred = model.predict(X)

    assert len(y_pred) == len(X), "Prediction length mismatch."
    assert isinstance(y_pred, (np.ndarray, list)), "Prediction output is not array or list."
