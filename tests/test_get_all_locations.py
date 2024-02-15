import requests
import pytest
from schemas.pydantic_schemas.info import InfoSchema
from schemas.pydantic_schemas.location import LocationSchema


# ENDPOINT: LOCATION
def test_get_all_locations():
    global response_data
    url = 'https://rickandmortyapi.com/api/location'
    count_locations = 0
    count_pages = 0

    while url:
        response = requests.get(url)
        response_data = response.json()
        InfoSchema(**response_data['info'])
        url = response_data['info']["next"]
        count_pages += 1
        assert response.status_code == 200, 'Wrong status code'

        if url:
            assert len(response_data['results']) == 20, 'Wrong count locations on page'
        else:
            assert len(response_data['results']) == 6, 'Wrong count locations on last page'

        for location in response_data['results']:
            LocationSchema(**location)
            count_locations += 1
        if count_pages == 1:
            assert response_data['info']['prev'] is None, 'Next page is available'
        if count_pages == 7:
            assert response_data['info']['next'] is None, 'Next page is available'
    else:
        assert response_data['info']['count'] == count_locations, 'Wrong count locations'
        assert response_data['info']['pages'] == count_pages, 'Wrong count pages'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_all_locations():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
