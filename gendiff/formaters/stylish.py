from itertools import chain


def stylish_view(diff, level=0, spaces_count=4):
    lines_to_output = []
    level_indent = ' ' * level * spaces_count
    level += 1
    for top_key, top_value in diff.items():
        type_ = top_value.get('type')
        value = top_value.get('value')
        old_value = top_value.get('from')
        new_value = top_value.get('to')
        if type_ == 'nested':
            lines_to_output.append(
                f"{level_indent}    {top_key}: {stylish_view(value, level)}")
        elif type_ == 'added':
            value = top_value.get('value')
            lines_to_output.append(
                f"{level_indent}  + {top_key}: {get_child(value, level)}")
        elif type_ == 'removed':
            lines_to_output.append(
                f"{level_indent}  - {top_key}: {get_child(value, level)}")
        elif type_ == 'changed':
            lines_to_output.append(
                f"{level_indent}  - {top_key}: {get_child(old_value, level)}")
            lines_to_output.append(
                f"{level_indent}  + {top_key}: {get_child(new_value, level)}")
        elif type_ == 'unchanged':
            lines_to_output.append(
                f"{level_indent}    {top_key}: {get_child(value, level)}")
        output_data = list(chain('{', lines_to_output, [level_indent + '}']))
    return '\n'.join(output_data)


def get_child(data, level=0, spaces_count=4):
    if not isinstance(data, dict):
        return data
    result = []
    level_indent = ' ' * level * spaces_count
    level += 1
    for key, value in data.items():
        result.append(
            f"{level_indent}    {key}: {get_child(value, level)}"
        )
    return '{\n' + '\n'.join(result) + '\n' + level_indent + '}'
