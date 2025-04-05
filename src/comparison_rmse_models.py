import matplotlib.pyplot as plt
import nbformat as nbf

# Load RMSE values for each model
xgboost_rmse = 0.9959832261071184
random_forest_rmse = 1.0797771831193614
least_squares_rmse = 1.7283776388154193  

# Create a bar plot to compare the models
models = ['XGBoost', 'Random Forest', 'Least Squares']
rmse_values = [xgboost_rmse, random_forest_rmse, least_squares_rmse]

plt.figure(figsize=(8, 5))
plt.bar(models, rmse_values, color=['blue', 'green', 'orange'])
plt.ylabel('RMSE')
plt.title('Comparison of Model Performance')

# Save the plot as a .png file
plot_path = "notebooks/rmse_comparison_plot.png"
plt.savefig(plot_path)
plt.close()

# Create a new Jupyter notebook to store the plot
nb = nbf.v4.new_notebook()

# Add markdown cell with a title
nb.cells.append(nbf.v4.new_markdown_cell("# Model Comparison: RMSE"))

# Add code cell to display the plot
nb.cells.append(nbf.v4.new_code_cell(f"from IPython.display import Image\nImage(filename='{plot_path}')"))

# Save the notebook in the 'notebooks' directory
notebook_path = "notebooks/comparison_rmse_model.ipynb"
with open(notebook_path, 'w') as f:
    nbf.write(nb, f)

print(f"Notebook saved at {notebook_path} with RMSE comparison plot.")
