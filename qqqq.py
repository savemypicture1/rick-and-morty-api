from pprint import pprint
import requests
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA

# ids = range(1, 827)
# response = requests.get(f'https://rickandmortyapi.com/api/character/{ids}')
# response_data = response.json()

for character_id in range(1, 827):
    url = f'https://rickandmortyapi.com/api/character/{character_id}'
    response = requests.get(url)
    response_data = response.json()
    validate(response_data, CHARACTER_SCHEMA)

    assert response.status_code == 200, 'Wrong status code'
    assert response_data['id'] == character_id, 'Wrong character id'


# while response:
#     response = response_data['info']["next"]
#     for character in response_data['results']:
#         print(response)
#         assert character['status'] == 'Alive'

# # print(type(response_data))
# validate(response_data['info'], INFO_SCHEMA)
# # for character in response_data['results']:
# #     validate(character, CHARACTER_SCHEMA)
#
# print(response.status_code)
# print(len(response_data['results']))
# print(response_data['results'])
