# Bengaluru House Price Prediction Project

## Table of Contents

1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Data Preprocessing](#data-preprocessing)
4. [Model Selection](#model-selection)
5. [Deployment](#deployment)
7. [Contributing](#contributing)

## Overview

This project aims to predict house prices in Bengaluru using machine learning. The dataset was obtained from Kaggle, and the analysis involves exploratory data analysis (EDA), data preprocessing, model selection, and deployment of the predictive model with a user-friendly UI.

## Project Structure

- `client`: Contains frontend files (HTML, CSS, JavaScript) for the user interface.
- `server`: Python Flask server to handle model predictions and serve the UI.
- `model`: Jupyter notebook and pickle file with the trained machine learning model.

## Data Preprocessing

- Performed Exploratory Data Analysis (EDA) on the Kaggle dataset.
- Removed columns with excessive missing values and those not relevant for the model.
- Addressed outliers and misleading data points.
- Checked and adjusted the distribution of columns in the dataset.
- Removed rows with misleading data.

## Model Selection

- Utilized GridSearchCV to identify the optimal machine learning algorithm.
- Tested Linear Regressor, Lasso, and Decision Tree algorithms with different parameters.
- Achieved the best accuracy with the Linear Regressor.

## Deployment

- Created a pickle file of the trained Linear Regression model.
- Developed a user-friendly UI using HTML, CSS, and JavaScript (provided in the `client` folder).
- Integrated the model with a Python Flask server (in the `server` folder) to deploy the prediction application.

## Contributing

- Contributions are welcome! If you'd like to contribute