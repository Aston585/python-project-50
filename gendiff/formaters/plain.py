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
                row.append(f"Property '{'.'.join([*path, item.get('key')])}' {changes}")  # noqa
        del path[-1:]
        output = '\n'.join(row)
        return output + '\n'

    return inner


def get_changes(data):
    if data.get('status') == 'added':
        added_value = wrap_value(data.get('value'))
        return f"was added with value: {added_value}"
    elif data.get('status') == 'removed':
        return "was removed"
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
