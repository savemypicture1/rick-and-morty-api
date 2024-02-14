import requests
import pytest
from jsonschema import validate
from schemas.base_page_schema import BASE_PAGE_SCHEMA
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA


# PAGES
@pytest.mark.xfail(reason="500 from the server")
def test_incorrect_page():
    response = requests.get('https://rickandmortyapi.com/api/character?page=43')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_page():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character?page=12')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character?page=25')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character?page=42')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
