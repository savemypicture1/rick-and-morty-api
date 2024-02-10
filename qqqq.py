from pprint import pprint
import requests

response = requests.get('https://rickandmortyapi.com/api/character/200,827')

response_data = response.json()
response_data2 = response.text
# pprint(len(response_data['results']))
pprint(response.status_code)
# print(type(response_data))
# print(type(response_data2))
pprint(response_data)
pprint(response_data['id'])
# print(response_data2)

# ids = [character['id'] for character in response_data]

# character_ids = []
# for character in response_data:
#     character_ids.append(character['id'])
# pprint(character_ids)
# assert response_data['count'] == 826
# assert response_data['pages'] == 42