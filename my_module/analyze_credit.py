import streamlit as st
import pandas as pd

def analyze_credit(test, encoded):
    
    features = encoded.columns

    # Get the list of available client IDs
    available_client_ids = test.index.tolist()

    # Determine the minimum and maximum client IDs
    min_client_id = test.index.min()
    max_client_id = test.index.max()

    # st.markdown(
    # f"<h1 style='color:#001f3f'>Prévision d'Approbation de Crédit et Analyse SHAP du Profil</h1>",
    # unsafe_allow_html=True
    # )

    # Initialize client_id and selected_score to default values
    default_client_id = available_client_ids[0]
    selected_score = 0.0

    # Add a text input for the user to enter a client ID
    client_id = st.selectbox('Select a client ID', available_client_ids, index=available_client_ids.index(default_client_id))
    # client_id = st.number_input('Enter a client ID', min_value=min(available_client_ids), max_value=max(available_client_ids), value=default_client_id, step=1)


    if client_id:
    # Validate that the entered client ID is within the valid range
        client_id = int(client_id)
        if client_id in available_client_ids:
            # Calculate the credit score and related information here
            selected_score = test[test.index == client_id]['Credit_score'].iloc[0]
        else:
            st.write("Veuillez entrer un numéro de client valide dans la plage spécifiée.")

        # Calculate the normalized distance
        threshold = 50
        distance = selected_score - threshold
        distance_normalisée = max(0.0, min(1.0, (distance + 100) / 200))

        # Define the color based on whether the score is accepted or not
        if distance >= 0:
            couleur = 'green'
            étiquette = 'Accepted'
            symbole = '✔️'
        else:
            couleur = 'red'
            étiquette = 'Rejected'
            symbole = '❌'

        # Display the credit score with the color, symbol, and label
        st.write(f"<p style='color:{couleur}'>Credit Score : <b>{selected_score:.2f}</b></p>", unsafe_allow_html=True)
        st.write(f"<p style='color:{couleur}'>{symbole} {étiquette}</p>", unsafe_allow_html=True)

        st.progress(distance_normalisée)

     


    return min_client_id, max_client_id, client_id, selected_score