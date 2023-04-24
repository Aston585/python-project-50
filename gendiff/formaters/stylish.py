from itertools import chain


def stylish_view(data):
    source = preparation_of_values(data)
    return stylish(source)


def preparation_of_values(data):
    row = []
    for item in data:
        if isinstance(item.get('value'), list):
            item = {'status': item.get('status'), 'key': item.get('key'),
                    'value': preparation_of_values(item.get('value'))}
        if isinstance(item.get('value'), dict):
            item['value'] = get_nested_object(item.get('value'))
        if item.get('status') == 'changing':
            item = [{'status': 'removed', 'key': item.get('key'),
                    'value': get_nested_object(item.get('from'))},
                    {'status': 'added', 'key': item.get('key'),
                    'value': get_nested_object(item.get('to'))}]
            row.extend(item)
            continue
        row.append(item)
    return row


def get_nested_object(data):
    if not isinstance(data, dict):
        return data
    result = []
    for key, value in data.items():
        result.append({'status': 'unchanging', 'key': key,
                       'value': get_nested_object(value)})
    return result


def stylish(data, replacer=' ', level=0, spaces_count=4):
    if not isinstance(data, list):
        return data
    level_indent = replacer * level * spaces_count
    level += 1
    row = []
    for item in data:
        status = retrieving_status(item.get('status'))
        output_state = status if status else replacer
        output_key = item.get('key')
        output_value = stylish(item.get('value'), level=level)
        row.append(f"{level_indent}  {output_state} {output_key}: {output_value}")  # noqa
    output_data = list(chain('{', row, [level_indent + '}']))
    return '\n'.join(output_data)


def retrieving_status(status_key):
    statuses = {'unchanging': ' ', 'added': '+', 'removed': '-'}
    return statuses.get(status_key)
