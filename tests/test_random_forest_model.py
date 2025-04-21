import os            # For checking if the model file exists
import joblib        # For loading the saved model from a .pkl file
import pandas as pd  # For reading the dataset
import numpy as np   # For checking prediction output type and shape


# Test 1: Check whether the Random Forest model file exists
def test_model_file_exists():
    """Check if the Random Forest .pkl file exists."""
    assert os.path.exists("../models/random_forest_model.pkl"), "Model file not found."
# Test 2: Load the model and check it's not None
def test_load_model():
    """Check that the model loads correctly."""
    model = joblib.load("../models/random_forest_model.pkl")
    assert model is not None, "Failed to load model."

# Test 3: Run predictions and validate the output
def test_model_prediction():
    """Test if the model can make predictions on known inputs."""
    df = pd.read_csv("../data/processed/cleaned_data.csv")
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]]
    
    model = joblib.load("../models/random_forest_model.pkl") # Load the trained Random Forest model
    y_pred = model.predict(X) # Use the model to make predictions

    assert len(y_pred) == len(X), "Prediction length mismatch." # Verify the number of predictions matches the number of inputs
    assert isinstance(y_pred, (np.ndarray, list)), "Prediction output is not array or list." # Confirm that the predictions are returned as a list or NumPy array
