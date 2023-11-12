from my_module.load_data_and_model import load_data_and_model
import lightgbm as lgb


def test_load_data_and_model():
    
    test, encoded, load_lgb = load_data_and_model()

    assert test.shape ==(48744,240)
    assert encoded.shape ==(48744,240)
    assert type(load_lgb)==lgb.sklearn.LGBMClassifier