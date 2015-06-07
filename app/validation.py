####
####

import jsonschema
from app import exceptions

create_random = {
    'type': 'object',
    'properties': {
        'length': {
            'type': 'integer',
            'minimum': 0,
            'maximum': 12,
        },
        'time_out': {
            'type': 'integer',
            'minimum': 1,
            'maximum': 65535,
        },
     },
     'required': ['length'],
     'additionalProperties': False,
}

def validate(ver_req, schema):
    json = ver_req.req
    try:
        jsonschema.validate(json, schema)
    except jsonschema.ValidationError as e:
        raise exceptions.inValidateInput(e.message)
