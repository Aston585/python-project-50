import json


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1:
        source1 = json.load(f1)
    with open(file_path2) as f2:
        source2 = json.load(f2)
    output = map(prepare_output_data,
            (i for i in get_comparison_results(source1, source2)))
    result = '\n'.join(output)
    return '{' + '\n' + result + '\n' + '}'



def get_comparison_results(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if key not in data2:
            result.append(('-', key, data1[key]))
        elif key in data1 and data2:
            if  data1[key] == data2[key]:
                result.append((' ', key,  data1[key]))
            elif data1[key] != data2[key]:
                result.append(('-', key,  data1[key]))
                result.append(('+', key, data2[key]))
        else:
            result.append(('+', key, data2[key]))
    return result


def prepare_output_data(data):
    status, key, value = data
    return f"{status} {key}: {value if value not in (False, True) else str(value).lower()}"
