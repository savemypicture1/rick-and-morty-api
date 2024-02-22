import requests

from schemas.pydantic_schemas.info import InfoSchema
from schemas.pydantic_schemas.location import ArrayLocation




class Locations():
    URL = 'https://rickandmortyapi.com/api/location'

    def get_all_locations(self):
        response = requests.get(self.URL)
        response_data = response.json()
        InfoSchema(**response_data['info'])
        ArrayLocation(**{'items': response_data['results']})

        return response, response_data
