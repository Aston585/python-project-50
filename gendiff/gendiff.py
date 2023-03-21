import json
import yaml
from itertools import chain


def chek_and_open_file(file_path):
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as f:
            file_yaml = yaml.safe_load(f)
            return file_yaml
    elif file_path.endswith('.json'):
        with open(file_path) as f:
            file_json = json.load(f)
            return file_json
    else:
        raise Exception("Invalid file format")


def generate_diff(file_path1, file_path2):
    source1 = chek_and_open_file(file_path1)
    source2 = chek_and_open_file(file_path2)
    diff = get_comparison_results(source1, source2)
    return stylish(diff)


def get_comparison_results(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if key not in data2:
            result.append(('-', key, data1[key]))
        elif key in data1 and data2:
            if not (isinstance(data1[key], dict)
                    and isinstance(data2[key], dict)):
                if data1[key] == data2[key]:
                    result.append((' ', key,  data1[key]))
                elif data1[key] != data2[key]:
                    result.append(('-', key,  data1[key]))
                    result.append(('+', key, data2[key]))
            else:
                result.append((' ', key,
                               get_comparison_results(data1[key], data2[key])))
        else:
            result.append(('+', key, data2[key]))
    return result


def stylish(data, replacer=' ', spaces_count=4):

    def inner(data, indent=0):
        if not isinstance(data, list):
            return data
        level = replacer * indent
        indent += spaces_count
        a = list(map(lambda data: f"{level}{replacer * spaces_count}"
                                  f"{data[0]} {data[1]}: "
                                  f"{normalize_value(inner(data[2], indent))}", data))  # noqa: E501
        b = list(chain('{', a, [level + '}']))
        return '\n'.join(b)

    return inner(data)


def normalize_value(data):
    if data is None:
        return 'null'
    if data not in (False, True):
        return data
    else:
        return str(data).lower()
