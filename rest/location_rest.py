import requests

from schemas.pydantic_schemas.info import InfoSchema
from schemas.pydantic_schemas.location import ArrayLocation, LocationSchema


class Locations():
    URL = 'https://rickandmortyapi.com/api/location'

    def get_all_locations(self):
        response = requests.get(self.URL)
        response_data = response.json()
        InfoSchema(**response_data['info'])
        ArrayLocation(**{'items': response_data['results']})

        return response, response_data

    def pagination(self, page_number):
        response = requests.get(f'{self.URL}?page={page_number}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})

        return response, response_data

    def get_location_by_id(self, id):
        response = requests.get(f'{self.URL}/{id}')
        response_data = response.json()
        if response.status_code == 200:
            LocationSchema(**response_data)

        return response, response_data