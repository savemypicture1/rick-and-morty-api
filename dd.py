import requests
from jsonschema import validate

qwe = [123, '123', 321]
wasd = {'www': 'aaa, ', 'eee': 'bbb'}
zxc = [222, '444', {'qwerty': 'wasd'}]
print(qwe)
print(wasd)
print(zxc)
print(type(qwe))
print(type(wasd))
print(type(zxc))
print(zxc[2])
print(zxc[2]['qwerty'])
print(len(zxc))

uuu = qwe[0] * qwe[2]
print(uuu)

# response = requests.get('https://rickandmortyapi.com/api')
# response_data = response.json()
# print(type(response_data))


# def test_filter_by_alive_status1():
#     global response_data
#     url = 'https://rickandmortyapi.com/api/character?status=alive'
#     count_characters = 0
#     count_pages = 0
#
#     while url:
#         response = requests.get(url)
#         response_data = response.json()
#         validate(response_data['info'], INFO_SCHEMA)
#         url = response_data['info']["next"]
#         count_pages += 1
#         assert response.status_code == 200, 'Wrong status code'
#
#         for character in response_data['results']:
#             validate(character, CHARACTER_SCHEMA)
#             count_characters += 1
#             assert character['status'] == 'Alive'
#         if count_pages == 1:
#             assert response_data['info']['prev'] is None, 'Next page is available'
#         if count_pages == 22:
#             assert response_data['info']['next'] is None, 'Next page is available'
#     else:
#         assert response_data['info']['count'] == 439, 'Wrong count characters'
#         assert count_characters == 439, 'Wrong count characters'
#         assert response_data['info']['pages'] == 22, 'Wrong count pages'
#         assert count_pages == 22, 'Wrong count pages'
