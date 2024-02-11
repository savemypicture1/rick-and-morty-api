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


response = requests.get('https://rickandmortyapi.com/api')
response_data = response.json()
print(type(response_data))
validate(response_data, BASE_PAGE_SCHEMA)