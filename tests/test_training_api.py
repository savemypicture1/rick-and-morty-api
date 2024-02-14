import requests
import pytest
from jsonschema import validate
from schemas.base_page_schema import BASE_PAGE_SCHEMA
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA


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
    response = requests.post('https://rickandmortyapi.com/api/character?page=20')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/character?page=20')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/character?page=20')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


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


# ENDPOINT: MULTIPLE CHARACTERS
def test_multiple_characters_id():
    response = requests.get('https://rickandmortyapi.com/api/character/1,826')
    response_data = response.json()
    character_ids = []
    for character in response_data:
        validate(character, CHARACTER_SCHEMA)
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
    validate(response_data, CHARACTER_SCHEMA)

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
        validate(character, CHARACTER_SCHEMA)
        character_ids.append(character['id'])

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == 1, 'Wrong count characters'
    assert character_ids[0] == 200, 'Wrong character id'


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


# ENDPOINT: LOCATION
