import requests

from schemas.pydantic_schemas.base_page import BasePageSchema


class BasePage():
    URL = 'https://rickandmortyapi.com/api'

    def send_request(self):
        response = requests.get('https://rickandmortyapi.com/api')
        response_data = response.json()
        BasePageSchema(**response_data)

        return response, response_data

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
