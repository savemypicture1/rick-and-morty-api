

from rest.location_rest import Locations


def test_get_all_locations():
    loc = Locations()
    response, response_data = loc.get_all_locations()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['info']['count'] == 126, 'Wrong count locations in info'
    assert response_data['info']['pages'] == 7, 'Wrong count pages in info'
    assert response_data['info']['prev'] is None, 'Prev page is available'
    assert response_data['info']['next'] is not None, 'Next page is available'
    assert len(response_data['results']) == 20, 'Wrong count locations on page'
