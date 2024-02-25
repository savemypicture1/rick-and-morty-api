from rest.base_url_rest_new import Base


# SEND REQUEST TO /BASE ENDPOINT
def test_base_url_new1():
    base_page = Base()
    base_page.send_request()
    base_page.validate_response_data()

    base_page.check_status_code(200)
    base_page.check_characters_url('character')
    base_page.check_locations_url('location')
    base_page.check_episodes_url('episode')


# SEND REQUEST TO /BASE ENDPOINT BY POST METHOD
def test_other_methods_base_page():
    base_page = Base()
    response, response_data = base_page.other_methods('post')

    assert response.status_code == 405, 'Wrong status code, must be 405 error'
    assert response_data['error'] == 'There is nothing here.'
