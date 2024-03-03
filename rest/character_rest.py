import requests

from schemas.pydantic_schemas.character import CharacterSchema, ArrayCharacter
from schemas.pydantic_schemas.info import InfoSchema


class Characters():
    URL = 'https://rickandmortyapi.com/api/character'

    def get_all_characters(self):
        response = requests.get(self.URL)
        response_data = response.json()
        InfoSchema(**response_data['info'])
        ArrayCharacter(**{'items': response_data['results']})

        return response, response_data

    def pagination(self, page_number):
        response = requests.get(f'{self.URL}?page={page_number}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})

        return response, response_data

    def get_character_by_id(self, id):
        response = requests.get(f'{self.URL}/{id}')
        response_data = response.json()
        if response.status_code == 200:
            CharacterSchema(**response_data)

        return response, response_data

    def get_multiple_characters(self, ids):
        response = requests.get(f'{self.URL}/{ids}')
        response_data = response.json()
        if response.status_code == 200:
            requested_ids = []
            ArrayCharacter(**{'items': response_data})
            for char in response_data:
                requested_ids.append(char['id'])
            assert requested_ids == ids, 'Ids does not match'

        return response, response_data

    def filter_by_name(self, name):
        response = requests.get(f'{self.URL}?name={name}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})

        return response, response_data

    def filter_by_name_page(self, page, name):
        response = requests.get(f'{self.URL}?page={page}&name={name}')
        response_data = response.json()

        if response.status_code == 200:
            names = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                names.append(char['name'])
            for requested_name in names:
                assert requested_name == name, 'Name does not match'

        return response, response_data

    def filter_by_status(self, status):
        response = requests.get(f'{self.URL}?status={status}')
        response_data = response.json()

        if response.status_code == 200:
            statuses = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                statuses.append(char['status'])
            for requested_status in statuses:
                assert requested_status == status, 'Status does not match'

        return response, response_data

    def filter_by_status_page(self, page, status):
        response = requests.get(f'{self.URL}?page={page}&status={status}')
        response_data = response.json()

        if response.status_code == 200:
            statuses = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                statuses.append(char['status'])
            for requested_status in statuses:
                assert requested_status == status, 'Status does not match'

        return response, response_data

    def filter_by_species(self, specie):
        response = requests.get(f'{self.URL}?species={specie}')
        response_data = response.json()

        if response.status_code == 200:
            species = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                species.append(char['species'])
            for requested_specie in species:
                assert requested_specie == specie, 'Species does not match'

        return response, response_data

    def filter_by_species_page(self, page, specie):
        response = requests.get(f'{self.URL}?page={page}&species={specie}')
        response_data = response.json()

        if response.status_code == 200:
            species = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                species.append(char['species'])
            for requested_specie in species:
                assert requested_specie == specie, 'Species does not match'

        return response, response_data

    def filter_by_type(self, type):
        response = requests.get(f'{self.URL}?type={type}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})

        return response, response_data

    def filter_by_type_page(self, page, type):
        response = requests.get(f'{self.URL}?page={page}&species={type}')
        response_data = response.json()
        if response.status_code == 200:
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})

        return response, response_data

    def filter_by_gender(self, gender):
        response = requests.get(f'{self.URL}?gender={gender}')
        response_data = response.json()

        if response.status_code == 200:
            genders = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                genders.append(char['gender'])
            for requested_gender in genders:
                assert requested_gender == gender, 'Genders does not match'

        return response, response_data

    def filter_by_gender_page(self, page, gender):
        response = requests.get(f'{self.URL}?page={page}&gender={gender}')
        response_data = response.json()

        if response.status_code == 200:
            genders = []
            InfoSchema(**response_data['info'])
            ArrayCharacter(**{'items': response_data['results']})
            for char in response_data['results']:
                genders.append(char['gender'])
            for requested_gender in genders:
                assert requested_gender == gender, 'Genders does not match'

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
