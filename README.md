# Credit_app

![Tests](https://github.com/isocan/Credit_app/actions/workflows/tests.yml/badge.svg)

# Credit Approval and SHAP Analysis App

This Streamlit application provides a user interface for analyzing credit approval and performing SHAP (SHapley Additive exPlanations) analysis on a machine learning model. The application is designed to load data, analyze credit information, and display SHAP values for a specific client.

## Project Structure

The project directory is organized as follows:

- **app.py**: The main Streamlit application script.
- **data/**: Directory containing input data files.
- **model/**: Directory containing the pre-trained machine learning model file (`lgbm_model.pkl`).
- **my_module/**: Custom Python modules for various functionalities.
- **tests/**: Directory containing unit tests for the custom modules.
- **Procfile, requirements.txt, runtime.txt, setup.sh**: Files for configuring the application on platforms like Heroku.

## Custom Modules

### 1. `load_data_and_model.py`

This module loads the input data (`df_application_test_subset.zip`, `X_encoded_subset.zip`) and the machine learning model (`lgbm_model.pkl`).

### 2. `analyze_credit.py`

Performs credit analysis on the loaded data and returns relevant information such as client IDs, credit scores, etc.

### 3. `calculate_shap_values.py`

Calculates SHAP values for a specific client using the loaded data and model.

### 4. `display_feature_analysis.py`

Displays feature analysis, showcasing the top SHAP values and their corresponding features for a given client.

## Running the Application

To run the Streamlit application locally, execute the following command in your terminal:

```bash
streamlit run app.py
