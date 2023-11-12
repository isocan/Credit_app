import pytest
from my_module.calculate_shap_values import calculate_shap_values

def test_calculate_shap_values(test_data_and_encoded, example_client_id):
    
    test, encoded, load_lgb = test_data_and_encoded
    
    example_features = encoded.columns.tolist()

    # Calculate SHAP values using the function
    shap_df = calculate_shap_values(test, encoded, load_lgb, example_client_id, example_features)

    # Define your assertions here based on expected behavior
    assert len(shap_df) == 10