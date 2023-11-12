import pandas as pd
import pickle
from zipfile import ZipFile

def load_data_and_model():
    with ZipFile('data/df_application_test_subset.zip', 'r') as zipf1:
        test = pd.read_csv(zipf1.open('df_application_test_subset.csv'), index_col='SK_ID_CURR')

    with ZipFile('data/X_encoded_subset.zip', 'r') as zipf2:
        encoded = pd.read_csv(zipf2.open('X_test_encoded_subset.csv'))

    # Load the lgb  model from a .pkl file
    with open('model/lgbm_model.pkl', 'rb') as model_file:
        load_lgb = pickle.load(model_file)
    
    return test, encoded, load_lgb