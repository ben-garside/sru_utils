import json
# from voluptuous import Schema
import logging


logger = logging.getLogger(__name__)


def jsonify(data, **kw):
    """ takes dictionary and converts to json, can add values to dict using kw
    """
    try:
        if len(kw.keys()) > 0:
            data.update(kw)
        return json.dumps(data)
    except Exception as e:
        print('we have Exception in jsonify', str(e))


def encode(data, encode="utf-8", json=False, **kw):
    if json:
        output = jsonify(data, **kw).encode(encode)
    else:
        output = data.encode(encode)
    return output


def same_type(field, expectedType):
    fieldType = type(field)
    if fieldType == expectedType:
        return True
    return False


def validator(fields, expected):
    """ Validate the data coming in requests
    """
    try:
        s = Schema(expected)
        return s(fields)
    except Exception as e:
        return e
    # fe = {
    #     'name': 'mohamed',
    #     'age': 'h'
    # }
    # ex = {
    #     'name': {
    #         'required': True,
    #         'default': None,
    #         'message': 'please provide a valid name',
    #         'type': str,
    #     }
    # }
    # msg = {}
    # exKeys = ex.keys()
    # feKeys = fe.keys()
    # for k in exKeys:
    #     msg.setdefault('required', False)
    #     msg.setdefault('default', None)
    #     msg.setdefault('message', '')
    #     msg.setdefault('type', str)
    #     if exKeys[k]['required'] and exKeys[k]['default'] is not None:
    #         pass