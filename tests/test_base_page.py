from rest.base_page_rest import BasePage


# SEND REQUEST TO /BASE ENDPOINT
def test_base_page():
    base_page = BasePage()
    response, response_data = base_page.send_request()

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['characters'] == 'https://rickandmortyapi.com/api/character', 'Wrong url'
    assert response_data['locations'] == 'https://rickandmortyapi.com/api/location', 'Wrong url'
    assert response_data['episodes'] == 'https://rickandmortyapi.com/api/episode', 'Wrong url'


# SEND REQUEST TO /BASE ENDPOINT BY POST METHOD
def test_other_methods_base_page():
    base_page = BasePage()
    response, response_data = base_page.other_methods('post')

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
