import shap
import pandas as pd

def calculate_shap_values(test, encoded, load_xgb, client_id, features):

    shap.initjs()
    
    explainer = shap.TreeExplainer(load_xgb)

    # Reset the index of the 'test' DataFrame
    
    test = test.reset_index()

    # Select the data for the specific client
    selected_data = encoded[encoded.index == test[test['SK_ID_CURR'] == client_id].index.values[0]]
    selected_data = selected_data.iloc[:, :]

    # Calculate the credit score and feature importance
    X_sample = selected_data.values.reshape(1, -1)
    shap_values = explainer.shap_values(X_sample)[0][0]

    # Compute absolute SHAP values
    abs_shap_values = [abs(val) for val in shap_values]

    # Sort the SHAP values and get the corresponding column indices
    sorted_indices = list(range(len(abs_shap_values)))
    sorted_indices.sort(key=lambda i: abs_shap_values[i], reverse=True)

    N = 10
    top_feature_indices = sorted_indices[:N]
    top_feature_names = [features[i] for i in top_feature_indices]
    top_feature_shap_values = [shap_values[i] for i in top_feature_indices]

    # Create a DataFrame for the top features and their SHAP values
    top_features_df = pd.DataFrame({'Feature': top_feature_names, 'SHAP Value': top_feature_shap_values})

    return top_features_df


