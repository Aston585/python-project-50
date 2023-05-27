from gendiff.loading import loading_data

#from gendiff.formaters.stylish import stylish_view
#from gendiff.formaters.plain import flatten
#from gendiff.formaters.json_ import json_viev


data1 = './tests/fixtures/file1.json'
data2 = './tests/fixtures/file2.json'


def generate_diff(data1, data2, format='stylish'):
    source1 = loading_data(data1)
    source2 = loading_data(data2)
    #diff = get_comparison_results(source1, source2)
    #if format == 'plain':
        #return flatten(diff)(diff)
    #elif format == 'json':
        #return json_viev(diff)
    pass
    #return stylish_view(diff)


print(generate_diff(data1, data2))









def get_comparison_results(data1, data2):
    keys = data1.keys() | data2.keys()
    result = []
    for key in sorted(keys):
        if (key in data1) and (key in data2):
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result.append({'status': 'nested',
                               'key': key,
                               'value': normalize_value(get_comparison_results(
                                        data1[key], data2[key]))})
            elif data1[key] == data2[key]:
                result.append({'status': 'unchanged',
                               'key': key,
                               'value': normalize_value(data1[key])})
            elif data1[key] != data2[key]:
                result.append({'status': 'changed',
                               'key': key,
                               'from': normalize_value(data1[key]),
                               'to': normalize_value(data2[key])})
        elif (key in data1) and (key not in data2):
            result.append({'status': 'removed',
                           'key': key,
                           'value': normalize_value(data1[key])})
        elif (key in data2) and (key not in data1):
            result.append({'status': 'added',
                           'key': key,
                           'value': normalize_value(data2[key])})
    return result


def normalize_value(data):
    if data is None:
        return 'null'
    if data not in (False, True):
        return data
    else:
        return str(data).lower()
