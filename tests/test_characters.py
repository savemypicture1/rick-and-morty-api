import requests
import pytest

from rest.character_rest import Characters
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


def test_filter_by_name_with_incorrect_page():
    name = Characters()
    response, response_data = name.filter_by_name_page(2, 'Rick Sanchez')

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
    status = Characters()
    response, response_data = status.filter_by_status_page(22, 'Alive')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 439, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 22, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 19, 'Wrong count characters on page'


def test_filter_by_alive_status_with_incorrect_page():
    status = Characters()
    response, response_data = status.filter_by_status_page(23, 'Alive')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


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
    status = Characters()
    response, response_data = status.filter_by_status_page(15, 'Dead')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 287, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 15, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 7, 'Wrong count characters on page'


def test_filter_by_dead_status_with_incorrect_page():
    status = Characters()
    response, response_data = status.filter_by_status_page(16, 'Dead')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


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
    status = Characters()
    response, response_data = status.filter_by_status_page(5, 'unknown')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 100, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 5, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_unknown_status_with_incorrect_page():
    status = Characters()
    response, response_data = status.filter_by_status_page(6, 'unknown')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_status():
    status = Characters()
    response, response_data = status.filter_by_status('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER CHARACTERS BY SPECIES
def test_filter_by_species():
    specie = Characters()
    response, response_data = specie.filter_by_species('Animal')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 55, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 3, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_species_last_page():
    specie = Characters()
    response, response_data = specie.filter_by_species_page(3, 'Animal')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 55, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 3, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 15, 'Wrong count characters on page'


def test_filter_by_species_with_incorrect_page():
    specie = Characters()
    response, response_data = specie.filter_by_species_page(4, 'Animal')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_species():
    specie = Characters()
    response, response_data = specie.filter_by_status('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER CHARACTERS BY TYPE
def test_filter_by_type():
    type = Characters()
    response, response_data = type.filter_by_type('Cromulon')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 1, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 1, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 1, 'Wrong count characters on page'


def test_filter_by_type_with_incorrect_page():
    type = Characters()
    response, response_data = type.filter_by_type_page(2, 'Cromulon')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_type():
    type = Characters()
    response, response_data = type.filter_by_type_page(2, 'qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER CHARACTERS BY GENDER
def test_filter_by_female_gender():
    gender = Characters()
    response, response_data = gender.filter_by_gender('Female')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 148, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 8, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_female_gender_last_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(8, 'Female')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 148, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 8, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 8, 'Wrong count characters on page'


def test_filter_by_female_gender_with_incorrect_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(9, 'Female')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_male_gender():
    gender = Characters()
    response, response_data = gender.filter_by_gender('Male')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 610, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 31, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_male_gender_last_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(31, 'Male')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 610, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 31, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 10, 'Wrong count characters on page'


def test_filter_by_male_gender_with_incorrect_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(32, 'Male')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_genderless_gender():
    gender = Characters()
    response, response_data = gender.filter_by_gender('Genderless')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 19, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 1, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 19, 'Wrong count characters on page'


def test_filter_by_genderless_gender_with_incorrect_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(2, 'Genderless')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_unknown_gender():
    gender = Characters()
    response, response_data = gender.filter_by_gender('unknown')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 49, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 3, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count characters on page'


def test_filter_by_unknown_gender_last_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(3, 'unknown')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 49, 'Wrong count characters in info'
    assert response_data['info']['pages'] == 3, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 9, 'Wrong count characters on page'


def test_filter_by_unknown_gender_with_incorrect_page():
    gender = Characters()
    response, response_data = gender.filter_by_gender_page(4, 'unknown')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_with_incorrect_gender():
    gender = Characters()
    response, response_data = gender.filter_by_gender('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# TEST WITH ALL FILTERS
def test_with_all_filters():
    pass


# SEND REQUEST TO CHARACTER ENDPOINTS BY OTHER METHODS
@pytest.mark.parametrize('methods', ['post', 'put', 'patch', 'delete'])
def test_other_methods_characters(methods):
    char = Characters()
    response, response_data = char.other_methods(methods)

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
