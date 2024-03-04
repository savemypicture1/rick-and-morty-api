import requests

from schemas.pydantic_schemas.character import CharacterSchema, ArrayCharacter
from schemas.pydantic_schemas.info import InfoSchema


class Characters():
    URL = 'https://rickandmortyapi.com/api/character'

    response = None
    response_data = None

    def send_request(self):
        self.response = requests.get(self.URL)
        self.response_data = self.response.json()

    def validate_response_data_info(self):
        InfoSchema(**self.response_data['info'])

    def validate_response_data_results(self):
        ArrayCharacter(**{'items': self.response_data['results']})

    def validate_character(self):
        CharacterSchema(**self.response_data)

    def check_status_code(self, status_code):
        assert self.response.status_code == status_code, 'Wrong status code'

    def check_response_data_info_count(self, count):
        assert self.response_data['info']['count'] == count, 'Wrong count characters in info'

    def check_response_data_info_pages(self, pages):
        assert self.response_data['info']['pages'] == pages, 'Wrong count pages in info'

    def check_prev_page_is_none(self):
        assert self.response_data['info']['prev'] is None, 'Prev page is available'

    def check_prev_page_is_not_none(self):
        assert self.response_data['info']['prev'] is not None, 'Next page is available'

    def check_next_page_is_none(self):
        assert self.response_data['info']['next'] is None, 'Next page is available'

    def check_next_page_is_not_none(self):
        assert self.response_data['info']['next'] is not None, 'Next page is available'

    def check_count_of_items_in_results(self, count):
        assert len(self.response_data['results']) == count, 'Wrong count characters on page'

    def send_request_with_page(self, page_number):
        self.response = requests.get(f'{self.URL}?page={page_number}')
        self.response_data = self.response.json()

    def check_error_message(self, message):
        assert self.response_data['error'] == message, 'Wrong error message'

    def get_character_by_id(self, id):
        self.response = requests.get(f'{self.URL}/{id}')
        self.response_data = self.response.json()

    def check_character_id(self, id):
        assert self.response_data['id'] == id, 'Wrong character id'

    def get_multiple_characters(self, ids):
        self.response = requests.get(f'{self.URL}/{ids}')
        self.response_data = self.response.json()

    def validate_multiple_characters(self):
        ArrayCharacter(**{'items': self.response_data})

    def check_response_multiple_ids(self, ids):
        requested_ids = []
        for char in self.response_data:
            requested_ids.append(char['id'])
        assert requested_ids == ids, 'Ids does not match'

    def filter_by_name(self, name):
        self.response = requests.get(f'{self.URL}?name={name}')
        self.response_data = self.response.json()

    def check_response_filter_by_name(self, name):
        for char in self.response_data['results']:
            assert char['name'] == name, 'Wrong character name'

    def filter_by_name_with_page(self, page, name):
        self.response = requests.get(f'{self.URL}?page={page}&name={name}')
        self.response_data = self.response.json()

    def filter_by_status(self, status):
        self.response = requests.get(f'{self.URL}?status={status}')
        self.response_data = self.response.json()

    def check_response_filter_by_status(self, status):
        statuses = []
        for char in self.response_data['results']:
            statuses.append(char['status'])
        for requested_status in statuses:
            assert requested_status == status, 'Status does not match'

    def filter_by_status_with_page(self, page, status):
        self.response = requests.get(f'{self.URL}?page={page}&status={status}')
        self.response_data = self.response.json()

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
