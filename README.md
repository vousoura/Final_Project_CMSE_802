# CMSE802 Project: Prediction of Dislocation Velocity in TaW Alloy Using ML

## Project Description

This project aims to use machine learning to predict the dislocation velocity in Tantalum-Tungsten (TaW) alloy, focusing on how solute atoms affect dislocation motion. Instead of using molecular dynamics simulations, I will use existing datasets and machine learning algorithms like XGBoost, Least Squares and Random Forest models to estimate the dislocation velocity based on parameters like solute concentration, temperature, slip plane and applied stress.

## Project Objectives

- **Data Collection & Preprocessing:** Load and clean the dataset.
- **Model Development:** Train the XGBoost regression model, the Least Squares and Random Forest models to predict dislocation velocity.
- **Model Evaluation:** Assess model performance using RMSE and visualization plots.
- **Data Visualization:** Plot results comparing dislocation velocity against parameters like stress, temperature, and W content.

## Project Directory Structure:

```text
Final_Project_CMSE_802/
├── src/                         # Source code for data processing and models
│   ├── data_processing.py       # Data loading and preprocessing functions
│   ├── Least_Squares_Model.py   # Least Squares Regression model
│   ├── Random_Forest_Model.py   # Random Forest Regression model
│   └── XGBoost_Model.py         # XGBoost Regression model
│
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
│   ├── test_data.py
│   └── test_model.py
│
├── results/                     # Output results and evaluation metrics
│   ├── least_squares_rmse.txt
│   ├── random_forest_rmse.txt
│   └── xgboost_rmse.txt
│
├── docs/                        # Project documentation
│   └── README.md
```
## Project Implementation:

```
My Dataset consists of 4 features:
├── Solute_Concentration       # Wt% of solute atoms
├── Slip_plane                 # Specific slip plane (110, 112, 123)
├── Temperature                # Temperature in Kelvin
├── Applied_stress             # External applied stress in MPa
└── Target: Velocity           # Dislocation velocity

My implementation Plan is:
├── Preprocessing:
│   ├── Load data from: data/raw/raw_data.xlsx
│   ├── Remove missing values
│   ├── Filter slip planes: 110, 112, 123
│   └── Save cleaned data to: data/processed/cleaned_data.csv
│
├── My model Training is:
│   ├── Split data: 75% train / 25% test
│   ├── Train models:
│   │   ├── Least Squares
│   │   ├── Random Forest
│   │   └── XGBoost            #I have only done this so far
│   └── Save models to: models/
│
└── Model Evaluation:
    ├── Compute RMSE for each model
    ├── Generate comparison plots
    └── Save results to: results/

├── Core Functionality:
│   └── Each script (in src/):
│       ├── Least_Squares_Model.py
│       ├── Random_Forest_Model.py
│       └── XGBoost_Model.py
│
│       Actions performed:
│       ├── Load cleaned dataset
│       ├── Split into train/test sets
│       ├── Train the model
│       ├── Save trained model to models/
│       └── Output RMSE to results/
│
├── Visualization and Analysis (in notebooks/):
│   ├── Scatter Plot: Actual vs Predicted Velocity (with regression line)
│   ├── Regression Plot: Applied Stress vs Predicted Velocity
│   ├── Regression Plot: Solute Concentration vs Predicted Velocity
│   ├── Regression Plot: Slip Plane vs Predicted Velocity
│   ├── Regression Plot: Temperature vs Predicted Velocity
│   ├── Histogram: Predicted Velocity
│   └── Box Plot: Predicted Velocity grouped by Solute Concentration
```
## Project Progress Assessment:

```
Project Progress Assessment:

├── I have successfully run the XGBoost regression model.
│   └── The model was trained on a dataset containing:
│       ├── Solute concentration
│       ├── Slip plane
│       ├── Temperature
│       └── Applied stress
│       as input features, with velocity as the target variable.

├── The dataset was preprocessed using data_processing.py
│   └── to clean and filter the necessary data.

├── The XGBoost model was trained and evaluated,
│   └── and I found the RMSE value to be: 0.99598.

└── I made the forementioned plots using Seaborn to analyze the model.
```


