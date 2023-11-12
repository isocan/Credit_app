import streamlit as st
import altair as alt

def display_feature_analysis(N, top_features_df, top_feature_names, test, client_id):
    st.write("Top {} Most Important Features:".format(N))

    # Create an Altair chart
    chart = alt.Chart(top_features_df).mark_bar().encode(
        x='SHAP Value',
        y=alt.Y('Feature', sort='-x'),
        color=alt.condition(
            alt.datum['SHAP Value'] > 0,
            alt.value('green'),  # Color for positive SHAP values
            alt.value('red')     # Color for negative SHAP values
        )
    ).properties(width=600, height=400)

    st.altair_chart(chart)

    # Create a dropdown to select a feature to plot
    selected_feature = st.selectbox("Select a feature to plot", top_feature_names)
     
    test = test.reset_index()
    
    # Include the data of the selected client
    selected_client_data = test[test['SK_ID_CURR'] == client_id].iloc[:, :-1]

    histogram = alt.Chart(test).mark_bar().encode(
        x=alt.X(selected_feature, bin=True),
        y='count()',
        color=alt.condition(
            alt.datum['SK_ID_CURR'] == client_id,
            alt.value('red'),  # Color for the selected client
            alt.value('blue')  # Color for other clients
        )
    ).properties(width=600, height=400)

    # Add a vertical line to indicate the position of the selected client's data
    vertical_line = alt.Chart(selected_client_data).mark_rule(color='red').encode(
        x=selected_feature
    )

    st.altair_chart(histogram + vertical_line)
