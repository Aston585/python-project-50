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
            result.append(('-', key, get_children(data1[key])))
        elif key in data1 and data2:
            if not (isinstance(data1[key], dict)
                    and isinstance(data2[key], dict)):
                if data1[key] == data2[key]:
                    result.append((' ', key,  get_children(data1[key])))
                elif data1[key] != data2[key]:
                    result.append(('-', key,  get_children(data1[key])))
                    result.append(('+', key, get_children(data2[key])))
            else:
                result.append((' ', key,
                               get_comparison_results(data1[key], data2[key])))
        else:
            result.append(('+', key, get_children(data2[key])))
    return result


def get_children(data):
    if not isinstance(data, dict):
        return data
    result = []
    for key, value in data.items():
        result.append((' ', key, get_children(value)))
    return result


def stylish(data, replacer=' ', level=0, spaces_count=4):
    if not isinstance(data, list):
        return data
    level_indent = replacer * level * spaces_count
    level += 1
    a = list(map(lambda data: f"{level_indent}  {data[0] if data[0] else replacer} {data[1]}: {normalize_value(stylish(data[2], level=level))}", data))  # noqa: E501
    b = list(chain('{', a, [level_indent + '}']))
    return '\n'.join(b)


def normalize_value(data):
    if data is None:
        return 'null'
    if data not in (False, True):
        return data
    else:
        return str(data).lower()
