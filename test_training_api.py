import requests
import pytest


# ENDPOINT: BASE_PAGE
def test_get_base_page():
    result = {
        'characters': 'https://rickandmortyapi.com/api/character',
        'locations': 'https://rickandmortyapi.com/api/location',
        'episodes': 'https://rickandmortyapi.com/api/episode'
    }

    response = requests.get('https://rickandmortyapi.com/api')
    response_data = response.json()

    assert response.status_code == 200, 'Wrong status code'
    assert result == response_data, 'Result does not match'


def test_post_base_page():
    response = requests.post('https://rickandmortyapi.com/api')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.'


# ENDPOINT: GET ALL CHARACTERS
def test_get_all_characters():
    response = requests.get('https://rickandmortyapi.com/api/character')
    response_data = response.json()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826
    assert response_data['info']['pages'] == 42
    assert len(response_data['results']) == 20


def test_post_get_all_characters():
    response = requests.post('https://rickandmortyapi.com/api/character')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'


# ENDPOINT: PAGES
def test_current_page():
    response = requests.get('https://rickandmortyapi.com/api/character/?page=2')
    response_data = response.json()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826
    assert response_data['info']['pages'] == 42


@pytest.mark.xfail(reason="500 from the server")
def test_incorrect_page():
    response = requests.get('https://rickandmortyapi.com/api/character/?page=43')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'


# ENDPOINT: GET A SINGLE CHARACTER
def test_get_a_single_character():
    response = requests.get('https://rickandmortyapi.com/api/character/5')
    response_data = response.json()
    character_id = response_data['id']

    assert response.status_code == 200, 'Wrong status code'
    assert character_id == 5


def test_get_incorrect_character_id():
    response = requests.get('https://rickandmortyapi.com/api/character/0')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


def test_get_incorrect_character_id2():
    response = requests.get('https://rickandmortyapi.com/api/character/827')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="500 from the server")
def test_get_incorrect_character_url():
    response = requests.get('https://rickandmortyapi.com/api/character/qwe')
    response_data = response.json()

    assert response.status_code == 400, 'Wrong status code'
    assert response_data['error'] == 'Hey! you must provide an id', 'Wrong/No error message'


def test_post_character_id():
    response = requests.post('https://rickandmortyapi.com/api/character/55')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'


# ENDPOINT: MULTIPLE CHARACTERS
def test_multiple_characters():
    response = requests.get('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()
    character_ids = []
    for character in response_data:
        character_ids.append(character['id'])

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == 2, 'Wrong count characters'
    assert character_ids[0] == 1
    assert character_ids[1] == 826


@pytest.mark.xfail(reason="200 from the server")
def test_negative_multiple_characters():
    response = requests.get('https://rickandmortyapi.com/api/character/0,827')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'


def test_single_correct_character():
    response = requests.get('https://rickandmortyapi.com/api/character/200,827')
    response_data = response.json()
    character_ids = []
    for character in response_data:
        character_ids.append(character['id'])

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == 1, 'Wrong count characters'
    assert character_ids[0] == 200


def test_post_multiple_characters():
    response = requests.post('https://rickandmortyapi.com/api/character/400,700')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here.', 'Wrong/No error message'
