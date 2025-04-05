import os
import joblib
import pandas as pd
import numpy as np

def test_model_file_exists():
    """Check if the Random Forest .pkl file exists."""
    assert os.path.exists("../models/random_forest_model.pkl"), "Model file not found."

def test_load_model():
    """Check that the model loads correctly."""
    model = joblib.load("../models/random_forest_model.pkl")
    assert model is not None, "Failed to load model."

def test_model_prediction():
    """Test if the model can make predictions on known inputs."""
    df = pd.read_csv("../data/processed/cleaned_data.csv")
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]]
    
    model = joblib.load("../models/random_forest_model.pkl")
    y_pred = model.predict(X)

    assert len(y_pred) == len(X), "Prediction length mismatch."
    assert isinstance(y_pred, (np.ndarray, list)), "Prediction output is not array or list."
