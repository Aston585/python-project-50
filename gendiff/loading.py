import json
import yaml
# BaseLoader используется для предотвращения неоднозначности соответствия
# значений, получаемым при десериализации: null -> None, '' -> None .
from yaml.loader import BaseLoader


def loading_data(file):
    if file.endswith('.yaml') or file.endswith('.yml'):
        with open(file) as f:
            file_content = yaml.load(f, Loader=BaseLoader)
            return number_to_int(file_content)
    elif file.endswith('.json'):
        with open(file) as f:
            return json.load(f)
    else:
        raise Exception("Invalid file format")


def number_to_int(data):
    for key, value in data.items():
        if isinstance(value, dict):
            number_to_int(value)
        else:
            if value == '0':
                data[key] = 0
            elif value.isdigit():
                data[key] = int(value)
    return data
