# CMSE802 Project: Prediction of Dislocation Velocity in TaW Alloy Using ML

## Project Description

This project aims to use machine learning to predict the dislocation velocity in Tantalum-Tungsten (TaW) alloy, focusing on how solute atoms affect dislocation motion. Instead of using molecular dynamics simulations, I will use existing datasets and machine learning algorithms like XGBoost, Least Squares and Random Forest models to estimate the dislocation velocity based on parameters like solute concentration, temperature, slip plane and applied stress.

## Project Objectives

- **Data Collection & Preprocessing:** Load and clean the dataset.
- **Model Development:** Train the XGBoost regression model, the Least Squares and Random Forest models to predict dislocation velocity.
- **Model Evaluation:** Assess model performance using RMSE and visualization plots.
- **Data Visualization:** Plot results comparing dislocation velocity against parameters like stress, temperature, and W content.

## Project Directory Structure:

Final_Project_CMSE_802/
│-- src/                   # Source code for the data processing and for the prediction models
│   │-- data_processing.py  # Data loading and preprocessing functions
│   │-- Least_Squares_Model.py  # Least Squares Regression model
│   │-- Random_Forest_Model.py  # Random Forest Regression model
│   │-- XGBoost_Model.py  # XGBoost Regression model
│
│-- notebooks/              # I am going to use Jupyter notebooks for analysis and visualization of the results for each model
│   │-- Least_Squares_Analysis.ipynb  # Plots for Least Squares
│   │-- Random_Forest_Analysis.ipynb  # Plots for Random Forest
│   │-- XGBoost_Analysis.ipynb  # Plots for XGBoost
│   │-- Model_Comparison.ipynb  # RMSE comparison across models
│
│-- data/                   # I am saving the datasets
│   │-- raw/                # Raw data files
│   │-- processed/          # Processed datasets
│
│-- models/                 # I am saving the trained models 
│   │-- least_squares_model.pkl  # Saved Least Squares model
│   │-- random_forest_model.pkl  # Saved Random Forest model
│   │-- xgboost_model.pkl  # Saved XGBoost model
│
│-- tests/                  # Unit tests
│   │-- test_data.py        # Testing data processing functions
│   │-- test_model.py       # Testing ML models
│
│-- results/                # Output results and figures
│   │-- least_squares_rmse.txt  # RMSE result for Least Squares
│   │-- random_forest_rmse.txt  # RMSE result for Random Forest
│   │-- xgboost_rmse.txt  # RMSE result for XGBoost
│
│-- docs/                   # Documentation
│   │-- README.md           # Project overview

- **Each model will be in a separate Python script in the src/ directory, and Jupyter notebooks in notebooks/ will be used for visualizing and analyzing the results. 
- **The models will be saved in the models/ directory, and the results for each model will be stored in results/.
