def flatten(diff, parent=None):
    lines_to_output = []

    for top_key, top_value in diff.items():
        path = f"{parent + '.' if parent else ''}{top_key}"

        if top_value.get('type') == 'nested':
            lines_to_output.append(flatten(top_value.get('value'), parent=path))  # noqa

        elif top_value.get('type') == 'added':
            added_property = wrap_value(top_value.get('value'))
            lines_to_output.append(
                f"Property '{path}' was added with value: {added_property}")

        elif top_value.get('type') == 'removed':
            lines_to_output.append(f"Property '{path}' was removed")

        elif top_value.get('type') == 'changed':
            previous_property = wrap_value(top_value.get('from'))
            new_property = wrap_value(top_value.get('to'))
            lines_to_output.append(
                f"Property '{path}' was updated."
                f" From {previous_property} to {new_property}")

    return '\n'.join(lines_to_output)


def wrap_value(data):
    if data in ['0']:
        return 0
    if isinstance(data, dict):
        return '[complex value]'
    elif data not in ('false', 'true', 'null'):
        return f"'{data}'"
    return data
