# CMSE802 Project: Prediction of Dislocation Velocity in TaW Alloy Using ML

## Project Description
This project aims to use machine learning to predict the dislocation velocity in Tantalum-Tungsten (TaW) alloy, focusing on how solute atoms affect dislocation motion. Instead of using molecular dynamics simulations, I use an existing dataset and train three models — XGBoost, Least Squares, and Random Forest — to predict dislocation velocity based on solute concentration, temperature, slip plane, and applied stress.

## Project Objectives
- **Data Collection & Preprocessing:** Load and clean the dataset.
- **Model Development:** Train the XGBoost, Least Squares, and Random Forest models to predict dislocation velocity.
- **Model Evaluation:** Assess model performance using RMSE and visualization plots.
- **Data Visualization:** Plot and analyze how dislocation velocity varies with solute concentration, slip plane, temperature, and stress.

## Project Directory Structure
```
Final_Project_CMSE_802/
├── src/                         # Source code for data processing and models
│   ├── data_processing.py       # Data loading and preprocessing functions
│   ├── Least_Squares_Model.py   # Least Squares Regression model
│   ├── Random_Forest_Model.py   # Random Forest Regression model
│   └── XGBoost_Model.py         # XGBoost Regression model
│   └── comparison_rmse_models.py  # comparison model
├── notebooks/                   # Jupyter notebooks for analysis and visualization
│   ├── Least_Squares_Analysis.ipynb   # Plots for Least Squares
│   ├── Random_Forest_Analysis.ipynb   # Plots for Random Forest
│   ├── XGBoost_Analysis.ipynb         # Plots for XGBoost
│   └── Model_Comparison.ipynb         # RMSE comparison across models
│
├── data/                        # Dataset storage
│   ├── raw/                     # Raw data files
│   └── processed/               # Processed datasets
│
├── models/                      # Saved trained models
│   ├── least_squares_model.pkl
│   ├── random_forest_model.pkl
│   └── xgboost_model.pkl
│
├── tests/                       # Unit tests
│   ├── test_XgBoost_model.py       # Tests for XGBoost model
│   ├── test_least_squares_model.py # Tests for Least Squares model
│   └── test_random_forest_model.py # Tests for Random Forest model
├── results/                     # Output results and evaluation metrics
│   ├── least_squares_rmse.txt
│   ├── random_forest_rmse.txt
│   └── xgboost_rmse.txt
│
├── docs/                        # Project documentation
│   └── README.md
```

## Project Implementation

### Dataset Features
The dataset consists of the following features:
- **Solute Concentration (Wt%)**
- **Slip Plane (110, 112, 123)**
- **Temperature (K)**
- **Applied Stress (MPa)**
- **Target Variable:** Dislocation Velocity

### Preprocessing
- Loaded data from `data/raw/raw_data.xlsx`
- Removed missing values
- Filtered slip planes (110, 112, 123)
- Saved cleaned data to `data/processed/cleaned_data.csv`

### Model Training
- Split data into 75% training / 25% testing
- Trained three models: Least Squares, Random Forest, XGBoost
- Saved models to `models/`

### Model Evaluation
- Computed RMSE for each model
- Created consistent plots across models
- Saved RMSE results to `results/`
- To ensure reliability and reproducibility, unit tests were implemented for each model and placed in the `tests/` directory. These include:
- `test_XgBoost_model.py`: Validates model training and output for XGBoost.
- `test_least_squares_model.py`: Confirms Least Squares model predictions and structure.
- `test_random_forest_model.py`: Checks prediction range and correctness for Random Forest.

Each test script verifies core functionality and helps maintain model robustness throughout development.


### Core Functionality
Each script in `src/`:
- Loads the cleaned dataset
- Splits into train/test sets
- Trains the model
- Saves the trained model to `models/`
- Outputs RMSE to `results/`

### Visualization and Analysis
Visualizations were created using Jupyter notebooks with Seaborn. Each model's results include:
- Scatter Plot: Actual vs Predicted Velocity
- Regression Plots: Velocity vs Applied Stress, Solute Concentration, Slip Plane, Temperature
- Histogram: Predicted Velocity Distribution
- Box Plot: Predicted Velocity by Solute Concentration

## Project Progress Assessment
- Successfully ran all three prediction models.
  - Trained on solute concentration, slip plane, temperature, and applied stress as features.
  - Velocity was the target variable.
- Dataset preprocessing was handled with `data_processing.py`
- Achieved RMSE value with all models.
- Plots were generated with Seaborn for analysis for all three models.

## Model Comparison Summary
Overall, the XGBoost and Random Forest models both demonstrated strong predictive performance, with the XGBoost model slightly outperforming the others in accuracy and consistency. Both tree-based models captured the expected physical trends: dislocation velocity decreased with increasing solute concentration and temperature, and varied slightly across slip planes — with slip planes 110 and 112 typically yielding higher predicted velocities. XGBoost produced
better actual vs. predicted velocity alignment, indicating strong model generalization, while Random Forest showed slightly more spread and variability. In contrast, the Least Squares model was able to capture basic linear relationships, such as the decrease in velocity with higher solute concentration and temperature. However, it struggled to model non-linear interactions, especially between velocity and slip plane. The predictions were more constrained, and the velocity distribution was narrower compared to the tree-based models. 

In conclusion, XGBoost provided the most robust and physically interpretable predictions across all key features, making it the most suitable model for predicting dislocation velocity in this dataset. Random Forest was a close second, while Least Squares, although useful for understanding linear trends, was limited in flexibility and predictive accuracy.

## References

- Kedharnath, A., Kapoor, R., and Sarkar, A. (2025). "Understanding dislocation velocity in TaW using explainable machine learning", 7, 327-336. :https://doi.org/10.1007/s42864-024-00306-9

- GitHub Repository (data and supplemental code):https://github.com/kedhar1992/dislocation-mobility/}
