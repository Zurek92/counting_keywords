user_json_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {'url': {'type': 'string', 'format': 'uri'}},
    'required': ['url'],
}
