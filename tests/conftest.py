import pytest
from my_module.load_data_and_model import load_data_and_model  # Import the functions you want to test

@pytest.fixture
def test_data_and_encoded():
    test, encoded, load_lgb = load_data_and_model()
    return test, encoded, load_lgb

@pytest.fixture
def example_client_id():
    # Define an example client ID (you can customize this)
    return 100005