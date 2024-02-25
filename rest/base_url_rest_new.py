import requests

from schemas.pydantic_schemas.base_url import BaseUrlSchema


class Base():
    URL = 'https://rickandmortyapi.com/api'

    response = None
    response_data = None

    def send_request(self):
        self.response = requests.get(self.URL)
        self.response_data = self.response.json()

    def validate_response_data(self):
        BaseUrlSchema(**self.response_data)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, 'Wrong status code'

    def check_characters_url(self, url):
        assert self.response_data['characters'] == f'{self.URL}/{url}', 'Wrong url'

    def check_locations_url(self, url):
        assert self.response_data['locations'] == f'{self.URL}/{url}', 'Wrong url'

    def check_episodes_url(self, url):
        assert self.response_data['episodes'] == f'{self.URL}/{url}', 'Wrong url'

    def other_methods(self, method):
        response = None
        if method == 'post':
            response = requests.post(self.URL)
        if method == 'put':
            response = requests.put(self.URL + '/148')
        if method == 'patch':
            response = requests.patch(self.URL + '/148')
        if method == 'delete':
            response = requests.delete(self.URL + '/148')
        response_data = response.json()

        return response, response_data
