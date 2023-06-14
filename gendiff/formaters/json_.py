import json


def json_viev(data):
    result = [json.dumps(data, indent=4)]
    return ''.join(result)
