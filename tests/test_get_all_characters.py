import requests
import pytest
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA


# ENDPOINT: GET ALL CHARACTERS
def test_get_all_characters():
    global response_data
    url = 'https://rickandmortyapi.com/api/character'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        if url:
            assert len(response_data['results']) == 20, 'Wrong count characters on page'
        else:
            assert len(response_data['results']) == 6, 'Wrong count characters on last page'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 42:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_all_characters():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'



