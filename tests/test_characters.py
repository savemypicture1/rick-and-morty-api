import requests
import pytest

from rest.character_rest import Characters
from schemas.pydantic_schemas.character import CharacterSchema
from utils.randomize_int import CharacterRandomize

randomizer = CharacterRandomize()


# SEND REQUEST TO /CHARACTER ENDPOINT
def test_get_all_characters():
    char = Characters()
    response, response_data = char.get_all_characters()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


# MANIPULATION WITH A CHARACTERS PAGES
@pytest.mark.parametrize('pages', [0, 1])
def test_first_pages(pages):
    page = Characters()
    response, response_data = page.pagination(pages)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


@pytest.mark.parametrize('pages', [randomizer.generate_random_page(),
                                   randomizer.generate_random_page()])
def test_valid_pages(pages):
    page = Characters()
    response, response_data = page.pagination(pages)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_last_page():
    page = Characters()
    response, response_data = page.pagination(42)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 6, 'Wrong count characters on page'


def test_not_exist_page():
    page = Characters()
    response, response_data = page.pagination(43)

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here'


# SEARCH CHARACTER BY ID
def test_get_character_by_valid_id():
    char = Characters()
    id = randomizer.generate_random_id()
    response, response_data = char.get_character_by_id(id)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == id, 'Wrong character id'


@pytest.mark.parametrize('id', [0, 827, 'qwerty'])
def test_get_character_by_invalid_id(id):
    char = Characters()
    response, response_data = char.get_character_by_id(id)

    if type(id) == int:
        assert response.status_code == 404, 'Wrong status code'
        assert response_data['error'] == 'Character not found', 'Wrong/No error message'
    else:
        assert response.status_code == 400, 'Wrong status code'
        assert response_data['error'] == 'Hey! you must provide an id', 'Wrong/No error message'


# SEARCH CHARACTERS BY MULTIPLE REQUEST
def test_get_valid_multiple_characters():
    char = Characters()
    ids = randomizer.generate_random_multiple_ids()
    response, response_data = char.get_multiple_characters(ids)

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == len(ids), 'Wrong count characters'


@pytest.mark.xfail(reason="200 from the server")
def test_invalid_multiple_characters():
    char = Characters()
    response, response_data = char.get_multiple_characters('0, 827')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Character not found', 'Wrong/No error message'


# FILTER CHARACTERS BY NAME
def test_filter_by_name():
    name = Characters()
    response, response_data = name.filter_by_name('Rick Sanchez')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 4, 'Wrong count characters'
    assert response_data['info']['pages'] == 1, 'Wrong count pages'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert response_data['info']['prev'] is None, 'Next page is available'
    assert len(response_data['results']) == 4, 'Wrong count characters on page'


def test_filter_by_name_with_invalid_page():
    name = Characters()
    response, response_data = name.filter_by_name('Rick Sanchez')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_name():
    name = Characters()
    response, response_data = name.filter_by_name('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER CHARACTERS BY STATUS
def test_filter_by_alive_status():
    status = Characters()
    response, response_data = status.filter_by_status('Alive')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 439, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 22, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_alive_status_last_page():
    page = Characters()
    response, response_data = page.filter_by_status_page(22, 'Alive')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 439, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 22, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 19, 'Wrong count characters on page'


# PAGES FOR FILTER BY DEAD STATUS
def test_filter_by_dead_status():
    status = Characters()
    response, response_data = status.filter_by_status('Dead')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 287, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 15, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_dead_status_last_page():
    page = Characters()
    response, response_data = page.filter_by_status_page(15, 'Dead')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 287, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 15, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 7, 'Wrong count characters on page'


# PAGES FOR FILTER BY UNKNOWN STATUS
def test_filter_by_unknown_status():
    status = Characters()
    response, response_data = status.filter_by_status('unknown')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 100, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 5, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_unknown_status_last_page():
    page = Characters()
    response, response_data = page.filter_by_status_page(5, 'unknown')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 100, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 5, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_incorrect_status():
    response = requests.get('https://rickandmortyapi.com/api/character?status=qwe1234')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# SEND REQUEST TO CHARACTER ENDPOINTS BY OTHER METHODS
@pytest.mark.parametrize('methods', ['post', 'put', 'patch', 'delete'])
def test_other_methods_characters(methods):
    char = Characters()
    response, response_data = char.other_methods(methods)

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


@pytest.mark.parametrize('pages', [randomizer.generate_random_page(), randomizer.generate_random_page()])
def test_valid_pages(pages):
    page = Characters()
    response, response_data = page.pagination(pages)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_last_page():
    page = Characters()
    response, response_data = page.pagination(42)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 826, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 42, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 6, 'Wrong count characters on page'


def test_invalid_page():
    page = Characters()
    response, response_data = page.pagination(43)

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here'
