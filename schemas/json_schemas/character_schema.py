
CHARACTER_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'status': {'type': 'string'},
        'species': {'type': 'string'},
        'type': {'type': 'string'},
        'gender': {'type': 'string'},
        'origin': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'url': {'type': 'string'}
            },
        },
        'location': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'url': {'type': 'string'}
            }
        },
        'image': {'type': 'string'},
        'episode': {
            'type': 'array',
            'items': {'type': 'string'}
        },
        'url': {'type': 'string'},
        'created': {'type': 'string', 'format': 'date-time'}
    },
    'required': ['id', 'name', 'status', 'species', 'type', 'gender', 'origin', 'location', 'image', 'episode', 'url', 'created']
}
