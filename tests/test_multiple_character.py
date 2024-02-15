import requests
import pytest
from schemas.pydantic_schemas.character import CharacterSchema


# ENDPOINT: MULTIPLE CHARACTERS
def test_multiple_characters_id():
    response = requests.get('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()
    character_ids = []
    for character in response_data:
        CharacterSchema(**character)
        character_ids.append(character['id'])

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == 2, 'Wrong count characters'
    assert character_ids[0] == 1, 'Wrong character id'
    assert character_ids[1] == 826, 'Wrong character id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_multiple_characters_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_ignore_zero_in_id():
    response = requests.get('https://rickandmortyapi.com/api/character/0745')
    response_data = response.json()
    CharacterSchema(**response_data)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 745, 'Wrong character id'


@pytest.mark.xfail(reason="200 from the server")
def test_negative_multiple_characters():
    response = requests.get('https://rickandmortyapi.com/api/character/0,827')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_negative_multiple_characters():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/0,827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/0,827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/0,827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_ignore_negative_multiple_character():
    response = requests.get('https://rickandmortyapi.com/api/character/200,827')
    response_data = response.json()
    character_ids = []
    for character in response_data:
        CharacterSchema(**character)
        character_ids.append(character['id'])

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == 1, 'Wrong count characters'
    assert character_ids[0] == 200, 'Wrong character id'
