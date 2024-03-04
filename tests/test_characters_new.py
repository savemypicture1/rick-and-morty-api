import pytest

from rest.character_rest_new import Characters
from utils.randomize_int import CharacterRandomize

randomizer = CharacterRandomize()


# SEND REQUEST TO /CHARACTER ENDPOINT
def test_get_all_characters():
    character = Characters()
    character.send_request()
    character.validate_response_data_info()
    character.validate_response_data_results()

    character.check_status_code(200)
    character.check_response_data_info_count(826)
    character.check_response_data_info_pages(42)
    character.check_prev_page_is_none()
    character.check_next_page_is_not_none()
    character.check_count_of_items_in_results(20)


# MANIPULATION WITH A CHARACTERS PAGES
@pytest.mark.parametrize('pages', [0, 1])
def test_first_pages(pages):
    character = Characters()
    character.send_request_with_page(pages)
    character.validate_response_data_info()
    character.validate_response_data_results()

    character.check_status_code(200)
    character.check_response_data_info_count(826)
    character.check_response_data_info_pages(42)
    character.check_prev_page_is_none()
    character.check_next_page_is_not_none()
    character.check_count_of_items_in_results(20)


@pytest.mark.parametrize('pages', [randomizer.generate_random_page(),
                                   randomizer.generate_random_page()])
def test_valid_pages(pages):
    character = Characters()
    character.send_request_with_page(pages)
    character.validate_response_data_info()
    character.validate_response_data_results()

    character.check_status_code(200)
    character.check_response_data_info_count(826)
    character.check_response_data_info_pages(42)
    character.check_prev_page_is_not_none()
    character.check_next_page_is_not_none()
    character.check_count_of_items_in_results(20)


def test_last_page():
    character = Characters()
    character.send_request_with_page(42)
    character.validate_response_data_info()
    character.validate_response_data_results()

    character.check_status_code(200)
    character.check_response_data_info_count(826)
    character.check_response_data_info_pages(42)
    character.check_prev_page_is_not_none()
    character.check_next_page_is_none()
    character.check_count_of_items_in_results(6)


def test_not_exist_page():
    character = Characters()
    character.send_request_with_page(43)

    character.check_status_code(404)
    character.check_error_message('There is nothing here')


# SEARCH CHARACTER BY ID
def test_get_character_by_valid_id():
    character = Characters()
    id = randomizer.generate_random_id()
    character.get_character_by_id(id)
    character.validate_character()

    character.check_status_code(200)
    character.check_character_id(id)


@pytest.mark.parametrize('id', [0, 827, 'qwerty'])
def test_get_character_by_invalid_id(id):
    character = Characters()
    character.get_character_by_id(id)

    if type(id) == int:
        character.check_status_code(404)
        character.check_error_message('Character not found')
    else:
        character.check_status_code(400)
        character.check_error_message('Hey! you must provide an id')


# SEARCH CHARACTERS BY MULTIPLE REQUEST
def test_get_valid_multiple_characters():
    character = Characters()
    ids = randomizer.generate_random_multiple_ids()
    character.get_multiple_characters(ids)
    character.validate_multiple_characters()

    character.check_status_code(200)
    character.check_response_multiple_ids(ids)


@pytest.mark.xfail(reason="200 from the server")
def test_get_invalid_multiple_characters():
    character = Characters()
    character.get_multiple_characters('0, 827')

    character.check_status_code(404)
    character.check_error_message('Character not found')


# FILTER CHARACTERS BY NAME
def test_filter_by_name():
    name = Characters()
    name.filter_by_name('Rick Sanchez')
    name.validate_response_data_info()
    name.validate_response_data_results()

    name.check_response_filter_by_name('Rick Sanchez')
    name.check_status_code(200)
    name.check_response_data_info_count(4)
    name.check_response_data_info_pages(1)
    name.check_next_page_is_none()
    name.check_prev_page_is_none()
    name.check_count_of_items_in_results(4)


def test_filter_by_name_with_incorrect_page():
    name = Characters()
    name.filter_by_name_with_page(2, 'Rick Sanchez')

    name.check_status_code(404)
    name.check_error_message('There is nothing here')


def test_filter_by_incorrect_name():
    name = Characters()
    name.filter_by_name('qwerty1234')

    name.check_status_code(404)
    name.check_error_message('There is nothing here')


# FILTER CHARACTERS BY STATUS
def test_filter_by_alive_status():
    status = Characters()
    status.filter_by_status('Alive')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('Alive')
    status.check_status_code(200)
    status.check_response_data_info_count(439)
    status.check_response_data_info_pages(22)
    status.check_prev_page_is_none()
    status.check_next_page_is_not_none()
    status.check_count_of_items_in_results(20)


def test_filter_by_alive_status_last_page():
    status = Characters()
    status.filter_by_status_with_page(22, 'Alive')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('Alive')
    status.check_status_code(200)
    status.check_response_data_info_count(439)
    status.check_response_data_info_pages(22)
    status.check_prev_page_is_not_none()
    status.check_next_page_is_none()
    status.check_count_of_items_in_results(19)


def test_filter_by_alive_status_with_incorrect_page():
    status = Characters()
    status.filter_by_status_with_page(23, 'Alive')

    status.check_status_code(404)
    status.check_error_message('There is nothing here')


def test_filter_by_dead_status():
    status = Characters()
    status.filter_by_status('Dead')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('Dead')
    status.check_status_code(200)
    status.check_response_data_info_count(287)
    status.check_response_data_info_pages(15)
    status.check_prev_page_is_none()
    status.check_next_page_is_not_none()
    status.check_count_of_items_in_results(20)


def test_filter_by_dead_status_last_page():
    status = Characters()
    status.filter_by_status_with_page(15, 'Dead')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('Dead')
    status.check_status_code(200)
    status.check_response_data_info_count(287)
    status.check_response_data_info_pages(15)
    status.check_prev_page_is_not_none()
    status.check_next_page_is_none()
    status.check_count_of_items_in_results(7)


def test_filter_by_dead_status_with_incorrect_page():
    status = Characters()
    status.filter_by_status_with_page(16, 'Dead')

    status.check_status_code(404)
    status.check_error_message('There is nothing here')


def test_filter_by_unknown_status():
    status = Characters()
    status.filter_by_status('unknown')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('unknown')
    status.check_status_code(200)
    status.check_response_data_info_count(100)
    status.check_response_data_info_pages(5)
    status.check_prev_page_is_none()
    status.check_next_page_is_not_none()
    status.check_count_of_items_in_results(20)


def test_filter_by_unknown_status_last_page():
    status = Characters()
    status.filter_by_status_with_page(5, 'unknown')
    status.validate_response_data_info()
    status.validate_response_data_results()

    status.check_response_filter_by_status('unknown')
    status.check_status_code(200)
    status.check_response_data_info_count(100)
    status.check_response_data_info_pages(5)
    status.check_prev_page_is_not_none()
    status.check_next_page_is_none()
    status.check_count_of_items_in_results(20)


def test_filter_by_unknown_status_with_incorrect_page():
    status = Characters()
    status.filter_by_status_with_page(6, 'unknown')

    status.check_status_code(404)
    status.check_error_message('There is nothing here')


def test_filter_by_incorrect_status():
    status = Characters()
    status.filter_by_status('qwerty1234')

    status.check_status_code(404)
    status.check_error_message('There is nothing here')


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
