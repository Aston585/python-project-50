from itertools import chain

data = [{'status': 'unchanging', 'key': 'common', 'value': [{'status': 'added', 'key': 'follow', 'value': 'false'}, {'status': 'unchanging', 'key': 'setting1', 'value': 'Value 1'}, {'status': 'removed', 'key': 'setting2', 'value': 200}, {'status': 'changing', 'key': 'setting3', 'from': 'true', 'to': 'null'}, {'status': 'added', 'key': 'setting4', 'value': 'blah blah'}, {'status': 'added', 'key': 'setting5', 'value': {'key5': 'value5'}}, {'status': 'unchanging', 'key': 'setting6', 'value': [{'status': 'unchanging', 'key': 'doge', 'value': [{'status': 'changing', 'key': 'wow', 'from': '', 'to': 'so much'}]}, {'status': 'unchanging', 'key': 'key', 'value': 'value'}, {'status': 'added', 'key': 'ops', 'value': 'vops'}]}]}, {'status': 'unchanging', 'key': 'group1', 'value': [{'status': 'changing', 'key': 'baz', 'from': 'bas', 'to': 'bars'}, {'status': 'unchanging', 'key': 'foo', 'value': 'bar'}, {'status': 'changing', 'key': 'nest', 'from': {'key': 'value'}, 'to': 'str'}]}, {'status': 'removed', 'key': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'status': 'added', 'key': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]


def preparation_of_values(data):
    row = []
    for item in data:
        if isinstance(item.get('value'), list):
           item = {'status': item.get('status'), 'key': item.get('key'), 'value': preparation_of_values(item.get('value'))}
        if isinstance(item.get('value'), dict):
            item['value'] = get_children(item.get('value'))
        if item.get('status') == 'changing':
            item = [{'status': 'removed', 'key': item.get('key'), 'value': get_children(item.get('from'))},{'status': 'added', 'key': item.get('key'), 'value': get_children(item.get('to'))}]
            row.extend(item)
            continue
        row.append(item)
    return row


def get_children(data):
    if not isinstance(data, dict):
        return data
    result = []
    for key, value in data.items():
        result.append({'status': 'unchanging', 'key': key, 'value': get_children(value)})
    return result



#data = [{'status': 'unchanging', 'key': 'common', 'value': [{'status': 'added', 'key': 'follow', 'value': 'false'}, {'status': 'unchanging', 'key': 'setting1', 'value': 'Value 1'}, {'status': 'removed', 'key': 'setting2', 'value': 200}, {'status': 'removed', 'key': 'setting3', 'value': 'true'}, {'status': 'added', 'key': 'setting3', 'value': 'null'}, {'status': 'added', 'key': 'setting4', 'value': 'blah blah'}, {'status': 'added', 'key': 'setting5', 'value': [{'status': 'unchanging', 'key': 'key5', 'value': 'value5'}]}, {'status': 'unchanging', 'key': 'setting6', 'value': [{'status': 'unchanging', 'key': 'doge', 'value': [{'status': 'removed', 'key': 'wow', 'value': ''}, {'status': 'added', 'key': 'wow', 'value': 'so much'}]}, {'status': 'unchanging', 'key': 'key', 'value': 'value'}, {'status': 'added', 'key': 'ops', 'value': 'vops'}]}]}, {'status': 'unchanging', 'key': 'group1', 'value': [{'status': 'removed', 'key': 'baz', 'value': 'bas'}, {'status': 'added', 'key': 'baz', 'value': 'bars'}, {'status': 'unchanging', 'key': 'foo', 'value': 'bar'}, {'status': 'removed', 'key': 'nest', 'value': [{'status': 'unchanging', 'key': 'key', 'value': 'value'}]}, {'status': 'added', 'key': 'nest', 'value': 'str'}]}, {'status': 'removed', 'key': 'group2', 'value': [{'status': 'unchanging', 'key': 'abc', 'value': 12345}, {'status': 'unchanging', 'key': 'deep', 'value': [{'status': 'unchanging', 'key': 'id', 'value': 45}]}]}, {'status': 'added', 'key': 'group3', 'value': [{'status': 'unchanging', 'key': 'deep', 'value': [{'status': 'unchanging', 'key': 'id', 'value': [{'status': 'unchanging', 'key': 'number', 'value': 45}]}]}, {'status': 'unchanging', 'key': 'fee', 'value': 100500}]}]

data = preparation_of_values(data)


def stylish(data, replacer=' ', level=0, spaces_count=4):
    if not isinstance(data, list):
        return data
    level_indent = replacer * level * spaces_count
    level += 1
    row = []
    for item in data:
        status = retrieving_status(item.get('status'))
        output_state =  status if status else replacer
        output_key = item.get('key')
        output_value = stylish(item.get('value'), level=level)
        row.append(f"{level_indent}  {output_state} {output_key}: {output_value}")
    output_data = list(chain('{', row, [level_indent + '}']))
    return '\n'.join(output_data)


def retrieving_status(status_key):
    statuses = {'unchanging': ' ', 'added': '+', 'removed': '-'}
    return statuses.get(status_key)


#print(preparation_of_values(data))
print(stylish(data))
