import json
import yaml


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
    output = map(prepare_output_data,
                 (i for i in get_comparison_results(source1, source2)))
    result = '\n'.join(output)
    return '{' + '\n' + result + '\n' + '}' + '\n'


def get_comparison_results(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if key not in data2:
            result.append(('-', key, data1[key]))
        elif key in data1 and data2:
            if data1[key] == data2[key]:
                result.append((' ', key,  data1[key]))
            elif data1[key] != data2[key]:
                result.append(('-', key,  data1[key]))
                result.append(('+', key, data2[key]))
        else:
            result.append(('+', key, data2[key]))
    return result


def prepare_output_data(data):
    status, key, value = data
    return f"  {status} {key}: {value if value not in (False, True) else str(value).lower()}"  # noqa: E501
