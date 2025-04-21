import os            # To check if the model file exists
import joblib        # To load the saved model file
import pandas as pd  # To read the cleaned CSV data
import numpy as np   # To verify the type and length of predictions

# Test 1: Check if the saved Least Squares model file exists in the models directory
def test_model_file_exists():
    """Check if the Least Squares .pkl file exists."""
    assert os.path.exists("../models/least_squares_model.pkl"), "Model file not found."

# Test 2: Attempt to load the Least Squares model from the .pkl file
def test_load_model():
    """Check that the Least Squares model loads correctly."""
    model = joblib.load("../models/least_squares_model.pkl")
    assert model is not None, "Failed to load Least Squares model."
# Test 3: Ensure the model can generate predictions on actual data
def test_model_prediction():
    """Test if the Least Squares model can make predictions."""
    df = pd.read_csv("../data/processed/cleaned_data.csv") # Load the dataset used during training or evaluation
    X = df[["Solute_Concentration", "Slip_plane", "Temperature", "Applied_stress"]] # Extract the input features for prediction

    model = joblib.load("../models/least_squares_model.pkl") # Load the trained model from file
    y_pred = model.predict(X) # Make predictions with the model on the input data

    assert len(y_pred) == len(X), "Prediction length mismatch." # Check if the number of predictions matches the number of input samples
    assert isinstance(y_pred, (np.ndarray, list)), "Prediction output is not array or list." # Confirm that the predictions are in a supported format
