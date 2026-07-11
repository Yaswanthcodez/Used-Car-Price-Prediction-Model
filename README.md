# Used Car Price Prediction 🚗

## Project Overview

This project predicts the price of a used car based on its specifications and characteristics using Machine Learning techniques.

The goal of the project was not only to build a prediction model but also to understand the complete end-to-end machine learning workflow including:

* Exploratory Data Analysis (EDA)
* Feature Engineering
* Missing Value Handling
* Encoding and Pipelines
* Model Training and Evaluation
* Deployment using Streamlit

---

## Problem Statement

Used car prices depend on multiple factors such as:

* Car age
* Brand
* Engine specifications
* Power and Torque
* Fuel type
* Transmission
* Kilometers driven
* Location
* Vehicle dimensions

Estimating a fair market value manually is difficult due to the interaction between these factors.

This project aims to automate the estimation process using Machine Learning.

---

## Dataset Information

The dataset contains information about used cars sold across multiple Indian cities.

### Features Used

#### Numerical Features

* Year
* Kilometer
* Engine
* Power
* Power RPM
* Torque
* Torque RPM
* Length
* Width
* Height
* Seating Capacity
* Fuel Tank Capacity

#### Categorical Features

* Make
* Fuel Type
* Transmission
* Location
* Color
* Seller Type
* Drivetrain
* Owner

### Target Variable

* Price

---

## Data Preprocessing

The following preprocessing steps were performed:

### Feature Engineering

* Converted `Engine` values from strings such as `1498 cc` into numeric values.
* Split `Max Power` into:

  * Power
  * Power RPM
* Split `Max Torque` into:

  * Torque
  * Torque RPM

### Missing Value Handling

* Removed rows with excessive missing values.
* Used group-wise imputation for important features.
* Used median or mean imputation where appropriate.

### Encoding

* One Hot Encoding for nominal categorical variables.
* Ordinal representation for ownership information.
* Implemented preprocessing using Scikit-Learn Pipelines and ColumnTransformer.

---

## Models Trained

### Linear Regression

* Train R²: 0.80
* Test R²: 0.66

### Decision Tree Regressor

* Train R²: 0.99
* Test R²: 0.81

### Random Forest Regressor

* Train R²: 0.97
* Test R²: 0.87

Random Forest achieved the best balance between bias and variance and was selected as the final model.

---

## Feature Importance

The model identified the following as the most important features:

1. Power
2. Torque
3. Kilometer
4. Fuel Tank Capacity
5. Year

Interestingly, Engine size and Make contributed less than expected because much of their information was already captured by Power and other numerical features.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Matplotlib
* Seaborn
* Streamlit
* Joblib

---

## Project Structure

```text
├── data/
├── notebook.ipynb
├── app.py
├── used_car_pipeline.pkl
├── requirements.txt
└── README.md
```

---

## Streamlit Application

The application allows users to enter car details and receive an estimated market price instantly.

Inputs include:

* Make
* Year
* Kilometers Driven
* Engine Specifications
* Fuel Type
* Transmission
* Drivetrain
* Dimensions
* Owner Information

Output:

* Predicted Used Car Price

---

## Key Learnings

This project helped in understanding:

* Real-world data preprocessing
* Missing value strategies
* Feature engineering
* Machine Learning pipelines
* Regression evaluation metrics
* Bias-Variance tradeoff
* Feature importance interpretation

---

## Future Improvements

Potential improvements include:

* Hyperparameter tuning
* Advanced encoding techniques
* Cross Validation
* XGBoost and LightGBM models
* Model deployment on cloud platforms
* Improved user interface for the web application

---

## By
Yaswanth
