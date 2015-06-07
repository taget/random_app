####
####

import jsonschema
from app import exceptions
from app import version_obj

max_ver = version_obj.version_obj('', '1.01')
min_ver = version_obj.version_obj('', '1.00')

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
    if ver_req < min_ver or ver_req > max_ver:
        raise exceptions.VersionNotSupport("Version %s not supported, min=%s,"
                                           "max=%s" % (ver_req, min_ver, max_ver))
    try:
        jsonschema.validate(json, schema)
    except jsonschema.ValidationError as e:
        raise exceptions.inValidateInput(e.message)
