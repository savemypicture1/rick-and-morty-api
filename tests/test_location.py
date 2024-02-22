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
def test_get_character_by_valid_id():
    loc = Locations()
    id = randomizer.generate_random_id()
    response, response_data = loc.get_location_by_id(id)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == id, 'Wrong character id'
