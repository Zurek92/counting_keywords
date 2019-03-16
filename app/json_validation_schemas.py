user_json_schema = {
    'type': 'object',
    'additionalProperties': False,
    'properties': {'url': {'type': 'string', 'format': 'uri'}, 'case_sensitive': {'type': 'boolean'}},
    'required': ['url', 'case_sensitive'],
}
