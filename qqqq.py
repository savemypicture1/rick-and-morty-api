from pprint import pprint
import requests
from jsonschema import validate
from schemas.character_schema import CHARACTER_SCHEMA

response = requests.get('https://rickandmortyapi.com/api/character')
response_data = response.json()



characters = []

# for character in response_data['results']:
#     characters.append(character)
#     validate(characters, CHARACTER_SCHEMA)

# pprint(characters)
# pprint(len(characters))
pprint(response_data['results'][1])

# assert response_data['count'] == 826
# assert response_data['pages'] == 42