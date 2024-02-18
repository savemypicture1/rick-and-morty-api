from pprint import pprint
import random

import requests

from rest.character_rest import Characters
from schemas.pydantic_schemas.character import CharacterSchema, ArrayCharacter
from schemas.pydantic_schemas.info import InfoSchema

response = requests.get('https://rickandmortyapi.com/api/character?status=alive')
response_data = response.json()
# print(response_data)
# print(response_data['results'])
for i, requested_status in enumerate(response_data['results']):
    print(i)
    # print(response_data['results'][i]['status'])
# if response.status_code == 200:
# InfoSchema(**response_data['info'])
# ArrayCharacter(**{'items': response_data['results']})
# for i, requested_status in enumerate(response_data['results']):
#     print(requested_status)
#     print(response_data['results']['status'])
#     print(response_data['results'][i]['status'])
#     assert requested_status[1] == response_data['results'][i]['status']

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
