import pytest

from rest.location_rest import Locations
from utils.randomize_int import LocationRandomize

randomizer = LocationRandomize()


# SEND REQUEST TO /LOCATION ENDPOINT
def test_get_all_locations():
    loc = Locations()
    response, response_data = loc.get_all_locations()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 126, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 7, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count locations on page'


@pytest.mark.parametrize('pages', [0, 1])
def test_first_pages(pages):
    loc = Locations()
    response, response_data = loc.pagination(pages)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 126, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 7, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count locations on page'


@pytest.mark.parametrize('pages', [randomizer.generate_random_page(),
                                   randomizer.generate_random_page()])
def test_valid_pages(pages):
    loc = Locations()
    response, response_data = loc.pagination(pages)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 126, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 7, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count locations on page'


def test_last_page():
    loc = Locations()
    response, response_data = loc.pagination(7)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 126, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 7, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 6, 'Wrong count locations on page'


def test_not_exist_page():
    loc = Locations()
    response, response_data = loc.pagination(8)

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here'


# SEARCH LOCATION BY ID
def test_get_locatiob_by_valid_id():
    loc = Locations()
    id = randomizer.generate_random_id()
    response, response_data = loc.get_location_by_id(id)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == id, 'Wrong location id'


@pytest.mark.parametrize('id', [127, 'qwerty'])
def test_get_location_by_invalid_id(id):
    loc = Locations()
    response, response_data = loc.get_location_by_id(id)

    if type(id) == int:
        assert response.status_code == 404, 'Wrong status code'
        assert response_data['error'] == 'Location not found', 'Wrong/No error message'
    else:
        assert response.status_code == 400, 'Wrong status code'
        assert response_data['error'] == 'Hey! you must provide an id', 'Wrong/No error message'


# SEARCH LOCATIONS BY MULTIPLE REQUEST
def test_get_valid_multiple_characters():
    loc = Locations()
    ids = randomizer.generate_random_multiple_ids()
    response, response_data = loc.get_multiple_locations(ids)

    assert response.status_code == 200, 'Wrong status code'
    assert len(response_data) == len(ids), 'Wrong count characters'


@pytest.mark.xfail(reason="200 from the server")
def test_invalid_multiple_characters():
    loc = Locations()
    response, response_data = loc.get_multiple_locations('0, 127')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Location not found', 'Wrong/No error message'


# FILTER LOCATIONS BY NAME
def test_filter_by_name():
    loc = Locations()
    response, response_data = loc.filter_by_name('Pawn Shop Planet')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 1, 'Wrong count locations'
    assert response_data['info']['pages'] == 1, 'Wrong count pages'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert response_data['info']['prev'] is None, 'Next page is available'
    assert response_data['results'][0]['name'] == 'Pawn Shop Planet', 'Wrong location name'
    assert len(response_data['results']) == 1, 'Wrong count locations on page'


def test_filter_by_name_with_incorrect_page():
    loc = Locations()
    response, response_data = loc.filter_by_name_page(2, 'Pawn Shop Planet')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_name():
    loc = Locations()
    response, response_data = loc.filter_by_name('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER LOCATIONS BY TYPE
def test_filter_by_type():
    loc = Locations()
    response, response_data = loc.filter_by_type('Planet')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 63, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 4, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count locations on page'


def test_filter_by_type_last_page():
    loc = Locations()
    response, response_data = loc.filter_by_type_page(4, 'Planet')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 63, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 4, 'Wrong count pages in info'
    assert response_data['info']['prev'] is not None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 3, 'Wrong count locations on page'


def test_filter_by_type_with_incorrect_page():
    loc = Locations()
    response, response_data = loc.filter_by_type_page(5, 'Planet')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_type():
    loc = Locations()
    response, response_data = loc.filter_by_type('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# FILTER LOCATIONS BY DIMENSION
def test_filter_by_dimension():
    loc = Locations()
    response, response_data = loc.filter_by_dimension('Dimension C-137')

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 5, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 1, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is None, 'Next page is available'
    assert len(response_data['results']) == 5, 'Wrong count locations on page'


def test_filter_by_dimension_with_incorrect_page():
    loc = Locations()
    response, response_data = loc.filter_by_dimension_page(2, 'Dimension C-137')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


def test_filter_by_incorrect_dimension():
    loc = Locations()
    response, response_data = loc.filter_by_dimension('qwerty1234')

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'There is nothing here', 'Wrong/No error message'


# SEND REQUEST TO LOCATION ENDPOINTS BY OTHER METHODS
@pytest.mark.parametrize('methods', ['post', 'put', 'patch', 'delete'])
def test_other_methods_characters(methods):
    loc = Locations()
    response, response_data = loc.other_methods(methods)

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
