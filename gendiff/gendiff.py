import json
import yaml
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import flatten


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


#data1 = chek_and_open_file('./tests/fixtures/file1.json')
#data2 = chek_and_open_file('./tests/fixtures/file2.json')


def generate_diff(file_path1, file_path2, format_name=None):
    source1 = chek_and_open_file(file_path1)
    source2 = chek_and_open_file(file_path2)
    diff = get_comparison_results(source1, source2)
    return flatten(diff) if format_name == 'plain' else stylish(diff)


def get_comparison_results(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if (key in data1) and (key in data2):
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append({'status': 'unchanging', 'key': key, 'value': normalize_value(get_comparison_results(data1[key], data2[key]))})
            elif data1[key] == data2[key]:
                result.append({'status': 'unchanging', 'key': key, 'value': normalize_value(data1[key])})
            elif data1[key] != data2[key]:
                result.append({'status': 'changing', 'key': key, 'from': normalize_value(data1[key]), 'to': normalize_value(data2[key])})
        elif (key in data1) and (key not in data2):
            result.append({'status': 'removed', 'key': key, 'value': normalize_value(data1[key])})
        elif (key in data2) and (key not in data1):
            result.append({'status': 'added', 'key': key, 'value': normalize_value(data2[key])})
    return result


def normalize_value(data):
    if data is None:
        return 'null'
    if data not in (False, True):
        return data
    else:
        return str(data).lower()


#print(get_comparison_results(data1, data2))
