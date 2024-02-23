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

    def get_multiple_locations(self, ids):
        response = requests.get(f'{self.URL}/{ids}')
        response_data = response.json()
        if response.status_code == 200:
            requested_ids = []
            ArrayLocation(**{'items': response_data})
            for loc in response_data:
                requested_ids.append(loc['id'])
            assert requested_ids == ids

        return response, response_data

    def filter_by_name(self, name):
        response = requests.get(f'{self.URL}?name={name}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})

        return response, response_data

    def filter_by_name_page(self, page, name):
        response = requests.get(f'{self.URL}?page={page}&name={name}')
        response_data = response.json()

        if response.status_code == 200:
            names = []
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})
            for loc in response_data['results']:
                names.append(loc['name'])
            for requested_name in names:
                assert requested_name == name

        return response, response_data

    def filter_by_type(self, type):
        response = requests.get(f'{self.URL}?type={type}')
        response_data = response.json()

        if response.status_code == 200:
            types = []
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})
            for loc in response_data['results']:
                types.append(loc['type'])
            for requested_type in types:
                assert requested_type == type

        return response, response_data

    def filter_by_type_page(self, page, type):
        response = requests.get(f'{self.URL}?page={page}&type={type}')
        response_data = response.json()

        if response.status_code == 200:
            types = []
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})
            for loc in response_data['results']:
                types.append(loc['type'])
            for requested_type in types:
                assert requested_type == type

        return response, response_data

    def filter_by_dimension(self, dimension):
        response = requests.get(f'{self.URL}?dimension={dimension}')
        response_data = response.json()

        if response.status_code == 200:
            dimensions = []
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})
            for loc in response_data['results']:
                dimensions.append(loc['dimension'])
            for requested_dimension in dimensions:
                assert requested_dimension == dimension

        return response, response_data

    def filter_by_dimension_page(self, page, dimension):
        response = requests.get(f'{self.URL}?page={page}&type={dimension}')
        response_data = response.json()

        if response.status_code == 200:
            dimensions = []
            InfoSchema(**response_data['info'])
            ArrayLocation(**{'items': response_data['results']})
            for loc in response_data['results']:
                dimensions.append(loc['dimension'])
            for requested_dimension in dimensions:
                assert requested_dimension == dimension

        return response, response_data

    def other_methods(self, method):
        response = None
        if method == 'post':
            response = requests.post(self.URL)
        if method == 'put':
            response = requests.put(self.URL + '/100')
        if method == 'patch':
            response = requests.patch(self.URL + '/100')
        if method == 'delete':
            response = requests.delete(self.URL + '/100')
        response_data = response.json()

        return response, response_data
