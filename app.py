import streamlit as st
from my_module.load_data_and_model import load_data_and_model
from my_module.analyze_credit import analyze_credit
from my_module.calculate_shap_values import calculate_shap_values
from my_module.display_feature_analysis import display_feature_analysis

# Load data and model
test, encoded, load_xgb = load_data_and_model()

# Main Streamlit app
def main():
    st.set_page_config(
        page_title="Credit Approval and SHAP Analysis",
        page_icon="🔍",
        layout="wide",
    )

    st.title("Credit Approval and SHAP Analysis App")

    min_client_id, max_client_id, client_id, selected_score = analyze_credit(test, encoded)

    st.write("---")

    # Display SHAP analysis for a specific client
    st.title("SHAP Analysis")


    # Calculate SHAP values
    top_features_df = calculate_shap_values(test, encoded, load_xgb, client_id, encoded.columns)

    # Display SHAP values
    display_feature_analysis(10, top_features_df, top_features_df['Feature'].values.tolist(), test, client_id)

if __name__ == "__main__":
    main()
