import requests
import pytest
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA


# FILTER CHARACTERS
def test_filter_by_name():
    response = requests.get('https://rickandmortyapi.com/api/character/?name=Rick Sanchez')
    response_data = response.json()
    validate(response_data['info'], INFO_SCHEMA)
    for character in response_data['results']:
        validate(character, CHARACTER_SCHEMA)
        assert character['name'] == 'Rick Sanchez', 'Wrong name'

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 4, 'Wrong count characters'
    assert response_data['info']['pages'] == 1, 'Wrong count pages'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert response_data['info']['prev'] is None, 'Next page is available'
    assert len(response_data['results']) == 4, 'Wrong count characters on page'


def test_filter_by_incorrect_name():
    response = requests.get('https://rickandmortyapi.com/api/character?status=qwe1234')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_filter_by_name():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character/?name=Rick Sanchez')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character/?name=Rick Sanchez')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character/?name=Rick Sanchez')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_filter_by_alive_status():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?status=alive'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['status'] == 'Alive'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 22:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_dead_status():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?status=dead'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['status'] == 'Dead'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 15:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_unknown_status():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?status=unknown'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['status'] == 'unknown'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 5:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_incorrect_status():
    response = requests.get('https://rickandmortyapi.com/api/character?status=qwe1234')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_filter_by_status():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/character?status=alive')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character?status=dead')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character?status=unknown')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_filter_by_species():
    pass


def test_filter_by_incorrect_species():
    pass


def test_filter_by_type():
    pass


def test_filter_by_incorrect_type():
    pass


def test_filter_by_female_gender():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?gender=female'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['gender'] == 'Female'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 8:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_male_gender():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?gender=male'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['gender'] == 'Male'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 31:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_genderless_gender():
    response = requests.get('https://rickandmortyapi.com/api/character?gender=genderless')
    response_data = response.json()
    count_characters = 0
    validate(response_data['info'], INFO_SCHEMA)

    for character in response_data['results']:
        validate(character, CHARACTER_SCHEMA)
        count_characters += 1
        assert character['gender'] == 'Genderless'

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == count_characters, 'Wrong count characters'
    assert response_data['info']['prev'] is None, 'Next page is available'
    assert response_data['info']['next'] is None, 'Next page is available'


def test_filter_by_unknown_gender():
    global response_data
    url = 'https://rickandmortyapi.com/api/character?gender=unknown'
    count_characters = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        validate(response_data['info'], INFO_SCHEMA)
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        for character in response_data['results']:
            validate(character, CHARACTER_SCHEMA)
            count_characters += 1
            assert character['gender'] == 'unknown'
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 3:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_characters, 'Wrong count characters'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


def test_filter_by_incorrect_gender():
    response = requests.get('https://rickandmortyapi.com/api/character?gender=qwe1234')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_with_all_filters():
    pass


def test_with_incorrect_query_parameter():
    response = requests.get('https://rickandmortyapi.com/api/character/?qwe=rick')
    response_data = response.json()
    validate(response_data['info'], INFO_SCHEMA)
    for character in response_data['results']:
        validate(character, CHARACTER_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters'
    assert response_data['info']['pages'] == 42, 'Wrong count pages'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'
