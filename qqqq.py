from pprint import pprint
import requests
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA

response = requests.get('https://rickandmortyapi.com/api/character')
response_data = response.json()

# pprint(response_data['info'])
# pprint(response_data['results'][])
print(response.status_code)
for chatacter in response_data['results']:
    validate(chatacter, CHARACTER_SCHEMA)

print(type(response_data))


# for item in response_data:
#     validate(response_data, CHARACTER_SCHEMA)



# characters = []

# for character in response_data['results']:
#     characters.append(character)
#     validate(characters, CHARACTER_SCHEMA)

# pprint(characters)
# pprint(len(characters))
# pprint(response_data['results'][1])

# assert response_data['count'] == 826
# assert response_data['pages'] == 42