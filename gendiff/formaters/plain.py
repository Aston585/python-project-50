#from itertools import chain

data = [{'status': 'unchanging', 'key': 'common', 'value': [{'status': 'added', 'key': 'follow', 'value': 'false'}, {'status': 'unchanging', 'key': 'setting1', 'value': 'Value 1'}, {'status': 'removed', 'key': 'setting2', 'value': 200}, {'status': 'changing', 'key': 'setting3', 'from': 'true', 'to': 'null'}, {'status': 'added', 'key': 'setting4', 'value': 'blah blah'}, {'status': 'added', 'key': 'setting5', 'value': {'key5': 'value5'}}, {'status': 'unchanging', 'key': 'setting6', 'value': [{'status': 'unchanging', 'key': 'doge', 'value': [{'status': 'changing', 'key': 'wow', 'from': '', 'to': 'so much'}]}, {'status': 'unchanging', 'key': 'key', 'value': 'value'}, {'status': 'added', 'key': 'ops', 'value': 'vops'}]}]}, {'status': 'unchanging', 'key': 'group1', 'value': [{'status': 'changing', 'key': 'baz', 'from': 'bas', 'to': 'bars'}, {'status': 'unchanging', 'key': 'foo', 'value': 'bar'}, {'status': 'changing', 'key': 'nest', 'from': {'key': 'value'}, 'to': 'str'}]}, {'status': 'removed', 'key': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'status': 'added', 'key': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]


def flatten(data):
    row = []
    path = []

    def inner(data):
        for item in data:
            if isinstance(item.get('value'), list):
                path.append(item.get('key'))
                inner(item.get('value'))
            changes = get_changes(item)
            if changes:
                row.append(f"Property '{'.'.join([*path, item.get('key')])}' {changes}")
        del path[-1:]
        return '\n'.join(row)

    return inner


def get_changes(data):
    if data.get('status') == 'added':
        added_value = wrap_value(data.get('value'))
        return f"was added with value: {added_value}"
    elif data.get('status') == 'removed':
        return f"was removed"
    elif data.get('status') == 'changing':
        changing_from = wrap_value(data.get('from'))
        changing_to = wrap_value(data.get('to'))
        return f"was updated. From {changing_from} to {changing_to}"


def wrap_value(data):
    if isinstance(data, dict):
        return '[complex value]'
    elif data not in ('false', 'true', 'null'):
        return f"'{data}'"
    return data


print(flatten(data)(data))
