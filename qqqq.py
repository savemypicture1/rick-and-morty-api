import requests
from schemas.pydantic_schemas.character import CharacterSchema

response = requests.get('https://rickandmortyapi.com/api/character/2')
response_data = response.json()
response_data['created'] = "qwerty"
CharacterSchema(**response_data)


# response_data = response.json()



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
print(response.status_code)
# print(len(response_data['results']))
# print(response_data['results'])
