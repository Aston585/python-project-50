def get_comparison_results(file1, file2):
    keys = file1.keys() | file2.keys()
    diff = {}
    for key in sorted(keys):
        if key not in file2:
            diff[key] = {'type': 'removed',
                         'value': convert_value(file1[key])}

        elif key not in file1:
            diff[key] = {'type': 'added',
                         'value': convert_value(file2[key])}

        elif isinstance(file1[key], dict) and isinstance(file2[key], dict):
            diff[key] = {'type': 'nested',
                         'value': get_comparison_results(file1[key], file2[key])}  # noqa

        elif file1[key] == file2[key]:
            diff[key] = {'type': 'unchanged',
                         'value': convert_value(file1[key])}

        elif file1[key] != file2[key]:
            diff[key] = {'type': 'changed',
                         'from': convert_value(file1[key]),
                         'to': convert_value(file2[key])}
    return diff


def convert_value(data):
    """
    Конвертирование значений после десериализации из json-файла.
    """
    if data is None:
        return 'null'
    if isinstance(data, bool):
        return str(data).lower()
    return data
