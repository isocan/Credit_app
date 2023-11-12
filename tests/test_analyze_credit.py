import pytest
from my_module.analyze_credit import analyze_credit

def test_analyze_credit(test_data_and_encoded):
    test_data, encoded_data, load_lgb = test_data_and_encoded

    # Define min and max client IDs and selected score
    min_client_id, max_client_id, client_id, selected_score = analyze_credit(test_data, encoded_data)

    # Define your assertions here based on expected behavior
    assert min_client_id == 100001
    assert max_client_id == 456250
    assert min_client_id <= client_id <= max_client_id, f"Selected client_id {client_id} is not between min and max values"
    assert 0 <= selected_score <= 100, f"Selected score {selected_score} is not between 0 and 100"
