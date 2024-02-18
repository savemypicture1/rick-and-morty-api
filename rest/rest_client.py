import requests


class RestClient:
    BASE_URL = 'https://rickandmortyapi.com/api/'

    def _get(self, path, params=None):
        url = self.BASE_URL + path
        response = requests.get(url, params)

        return response.json()

    def _post(self):
        pass

    def _put(self):
        pass

    def _delete(self):
        pass
