import requests
import pytest
from schemas.pydantic_schemas.location import LocationSchema


# PARAMETRIZE (0, 1, 80, 126, 127) !!!!!!!!!!!!!!!!
# ENDPOINT: GET A SINGLE LOCATION
@pytest.mark.xfail(reason="200 from the server")
def test_min_negative_location_id():
    response = requests.get('https://rickandmortyapi.com/api/location/0')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Location not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_min_negative_location_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/0')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_first_location_id():
    response = requests.get('https://rickandmortyapi.com/api/location/1')
    response_data = response.json()
    LocationSchema(**response_data)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 1, 'Wrong location id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_first_location_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/1')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_single_location():
    response = requests.get('https://rickandmortyapi.com/api/location/80')
    response_data = response.json()
    LocationSchema(**response_data)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 80, 'Wrong location id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_single_location():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location/80')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/80')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/80')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_get_a_last_location_id():
    response = requests.get('https://rickandmortyapi.com/api/location/126')
    response_data = response.json()
    LocationSchema(**response_data)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == 126, 'Wrong location id'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_for_a_last_location_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location/126')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/126')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/126')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


def test_max_negative_location_id():
    response = requests.get('https://rickandmortyapi.com/api/location/127')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Location not found', 'Wrong/No error message'


@pytest.mark.xfail(reason="404 error instead 405 for other methods")
def test_parametrize_methods_with_negative_location_id():
    # Parametrize methods
    response = requests.post('https://rickandmortyapi.com/api/location/127')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/127')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/127')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'


@pytest.mark.skip('Create For fun')
def test_id_for_all_locations():
    for location_id in range(1, 127):
        url = f'https://rickandmortyapi.com/api/location/{location_id}'
        response = requests.get(url)
        response_data = response.json()
        LocationSchema(**response_data)

        assert response.status_code == 200, 'Wrong status code'
        assert response_data['id'] == location_id, 'Wrong location id'


@pytest.mark.xfail(reason="Wrong status code")
def test_parametrize_methods_with_incorrect_location_id():
    # Parametrize methods
    response = requests.get('https://rickandmortyapi.com/api/location/qwerty')
    response_data = response.json()

    assert response.status_code == 404, 'Wrong status code'
    assert response_data['error'] == 'Hey! you must provide an id', 'Wrong/No error message'

    response = requests.post('https://rickandmortyapi.com/api/location/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.put('https://rickandmortyapi.com/api/location/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'

    response = requests.delete('https://rickandmortyapi.com/api/location/qwerty')
    response_data = response.json()

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
