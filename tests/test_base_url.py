from rest.base_url_rest import Base


# SEND REQUEST TO /BASE ENDPOINT
def test_base_url():
    base_page = Base()
    response, response_data = base_page.send_request()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['characters'] == 'https://rickandmortyapi.com/api/character', 'Wrong url'
    assert response_data['locations'] == 'https://rickandmortyapi.com/api/location', 'Wrong url'
    assert response_data['episodes'] == 'https://rickandmortyapi.com/api/episode', 'Wrong url'


def test_base_url_new():
    base_page = Base()
    base_page.send_request()
    base_page.validate_response_data()

    assert base_page.response.status_code == 200
    assert base_page.response_data['characters'] == f'{base_page.URL}/character', 'Wrong url'
    assert base_page.response_data['locations'] == f'{base_page.URL}/location', 'Wrong url'
    assert base_page.response_data['episodes'] == f'{base_page.URL}/episode', 'Wrong url'


def test_base_url_new1():
    base_page = Base()
    base_page.send_request()
    base_page.validate_response_data()

    base_page.check_status_code(200)
    base_page.check_characters_url()
    base_page.check_locations_url()
    base_page.check_episodes_url()


# SEND REQUEST TO /BASE ENDPOINT BY POST METHOD
def test_other_methods_base_page():
    base_page = Base()
    response, response_data = base_page.other_methods('post')

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
