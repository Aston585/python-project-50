import json


def json_viev(data):
    result = [json.dumps(data, indent=4), '\n']
    return ''.join(result)
