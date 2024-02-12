
INFO_SCHEMA = {
    'type': 'object',
    'properties': {
        'count': {'type': 'integer'},
        'next': {'type': ['string', 'null']},
        'pages': {'type': 'integer'},
        'prev': {'type': ['string', 'null']}
    },
    'required': ['count', 'next', 'pages', 'prev']
}
