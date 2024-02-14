import requests
import pytest
from jsonschema import validate
from schemas.base_page_schema import BASE_PAGE_SCHEMA


# ENDPOINT: BASE_PAGE
def test_base_page():
    result = {
        'characters': 'https://rickandmortyapi.com/api/character',
        'locations': 'https://rickandmortyapi.com/api/location',
        'episodes': 'https://rickandmortyapi.com/api/episode'
    }

    response = requests.get('https://rickandmortyapi.com/api')
    response_data = response.json()
    validate(response_data, BASE_PAGE_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert result == response_data, 'Result does not match'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_base_page():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
