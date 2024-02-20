from pprint import pprint
import random

import requests

from rest.character_rest import Characters
from schemas.pydantic_schemas.character import CharacterSchema, ArrayCharacter
from schemas.pydantic_schemas.info import InfoSchema

response = requests.get('https://rickandmortyapi.com/api/character?type=Cromulon')
response_data = response.json()
print(response.status_code)
pprint(response_data)
# pprint(type(page))

# response = requests.get('https://rickandmortyapi.com/api/character?status=alive')
# response_data = response.json()
# status = []
# for char in response_data['results']:
#     status.append(char['status'])
# print(status)

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
