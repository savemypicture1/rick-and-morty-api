from pprint import pprint
import random

import requests

from rest.character_rest_new import Characters
from schemas.pydantic_schemas.character import CharacterSchema, ArrayCharacter
from schemas.pydantic_schemas.info import InfoSchema
from utils.randomize_int import CharacterRandomize

# randomizer = CharacterRandomize()
#
# character = Characters()
# ids = randomizer.generate_random_multiple_ids()
# character.get_multiple_characters(ids)
# character.validate_multiple_characters()
# print(ids)
# print(type(ids))
# print(character)

# assert response.status_code == 200, 'Wrong status code'
# assert len(response_data) == len(ids), 'Wrong count characters'


response = requests.get('https://rickandmortyapi.com/api/character/?type=Cromulon')
response_data = response.json()
print(response.status_code)
pprint(response_data)



# response = requests.get('https://rickandmortyapi.com/api/character?name=Rick Sanchez')
# response_data = response.json()
# # names = []
# for char in response_data['results']:
#     # names.append(char['name'])
#     assert char['name'] == 'Rick Sanchez', 'Wrong character name'
# print(names)

# input_ids = '20', '22', '826'
# response = requests.get(f'https://rickandmortyapi.com/api/character/{input_ids}')
# response_data = response.json()
# ids = []
# for char in response_data:
#     ids.append(char['id'])
# print(ids)
# print(type(input_ids))

# response = requests.get(f'{self.URL}/{",".join(map(str, ids))}')


# def get_multiple_characters(*ids):
#     idss = ",".join(map(str, ids))
#     print(idss)
#     print(type(idss))


# get_multiple_characters(15, 20, 700)
#
# multiple_ids = []
# for _ in range(1, random.randint(2, 826)):
#     multiple_ids.append(random.randint(1, 826))
# print(set(multiple_ids))
# print(type(set(multiple_ids)))
# print(list(set(multiple_ids)))
# print(type(list(set(multiple_ids))))
# print(sorted(list(set(multiple_ids))))
# print(type(sorted(list(set(multiple_ids)))))
# print(multiple_ids)
# print(type(multiple_ids))
