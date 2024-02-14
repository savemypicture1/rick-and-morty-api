import requests
import pytest
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA


# PARAMETRIZE (0, 1, 400, 826, 827) !!!!!!!!!!!!!!!!
# ENDPOINT: GET A SINGLE CHARACTER
def test_min_negative_character_id():
    response = requests.get('https://rickandmortyapi.com/api/character/0')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_min_negative_character_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_first_character_id():
    response = requests.get('https://rickandmortyapi.com/api/character/1')
    response_data = response.json()
    validate(response_data, CHARACTER_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 1, 'Wrong character id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_first_character_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_single_character():
    response = requests.get('https://rickandmortyapi.com/api/character/400')
    response_data = response.json()
    validate(response_data, CHARACTER_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 400, 'Wrong character id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_single_character():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/400')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/400')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/400')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_last_character_id():
    response = requests.get('https://rickandmortyapi.com/api/character/826')
    response_data = response.json()
    validate(response_data, CHARACTER_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 826, 'Wrong character id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_last_character_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/826')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_max_negative_character_id():
    response = requests.get('https://rickandmortyapi.com/api/character/827')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_negative_character_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/827')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


@pytest.mark.skip('Create For fun')
def test_id_for_all_characters():
    for character_id in range(1, 827):
        url = f'https://rickandmortyapi.com/api/character/{character_id}'
        response = requests.get(url)
        response_data = response.json()
        validate(response_data, CHARACTER_SCHEMA)

        assert response.status_code == 200, 'Wrong status code'
        assert response_data['id'] == character_id, 'Wrong character id'


@pytest.mark.xfail(reason="Wrong status code")
def test_parametrize_methods_with_incorrect_character_id():
    # Parametrize methods
    response = requests.get('https://rickandmortyapi.com/api/character/qwerty')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Hey! you must provide an id', 'Wrong/No error message'

    response = requests.post('https://rickandmortyapi.com/api/character/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
