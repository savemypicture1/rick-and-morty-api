BASE_URL_SCHEMA = {
    'type': 'object',
    'properties': {
        'characters': {'type': 'string'},
        'locations': {'type': 'string'},
        'episodes': {'type': 'string'}
    },
    'required': ['characters', 'locations', 'episodes']
}
