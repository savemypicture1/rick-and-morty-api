
CHARACTER_SCHEMA = {
    'type': 'object',
    'properties': {
        'id': {'type': 'integer'},
        'name': {'type': 'string'},
        'status': {'type': 'string'},
        'species': {'type': 'string'},
        'type': {'type': 'string', 'nullable': True},
        'gender': {'type': 'string'},
        'origin': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string'},
                'url': {'type': 'string', 'nullable': True}
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
        'created': {'type': 'string'}
    }
}
