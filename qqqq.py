from pprint import pprint
import requests
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA
from schemas.info_schema import INFO_SCHEMA



response = requests.get('https://rickandmortyapi.com/api/character?status=123')
response_data = response.json()
pprint(response_data)


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
