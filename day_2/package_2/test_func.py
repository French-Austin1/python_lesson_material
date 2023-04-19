import pytest, random
from unittest.mock import Mock
import requests


def generate_random_phonenumber():
    '''Generate a random phone number with 10 digits and a 503 area code'''
    return f'503-{random.randint(100,999)}-{random.randint(1000,9999)}'

def test_generate_random_phonenumber():
    '''Test the generate_random_phonenumber() function'''
    assert len(generate_random_phonenumber()) == 14
    assert generate_random_phonenumber()[0:3] == '503'


# simple test with fixture
@pytest.fixture 
def example_fixture():
    return 1

def test_example_fixture(example_fixture):
    assert example_fixture == 1

# perameterized test with fixture
@pytest.mark.parametrize("test_input, expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])

def test_perameterized(test_input, expected):
    assert eval(test_input) == expected # eval() is a built-in function that evaluates a string as a Python expression


def test_request_mock():
    '''Mocking a request and looking for a 200 response'''
    mock_response = Mock()
    mock_response.status_code = 200
    requests.get = Mock(return_value=mock_response)
    response = requests.get('https://www.google.com')
    assert response.status_code == 200
