#data = [{'status': 'unchanging', 'key': 'common', 'value': [{'status': 'added', 'key': 'follow', 'value': False}, {'status': 'unchanging', 'key': 'setting1', 'value': 'Value 1'}, {'status': 'removed', 'key': 'setting2', 'value': 200}, {'status': 'changing', 'key': 'setting3', 'from': True, 'to': 'null'}, {'status': 'added', 'key': 'setting4', 'value': 'blah blah'}, {'status': 'added', 'key': 'setting5', 'value': {'key5': 'value5'}}, {'status': 'unchanging', 'key': 'setting6', 'value': [{'status': 'unchanging', 'key': 'doge', 'value': [{'status': 'changing', 'key': 'wow', 'from': '', 'to': 'so much'}]}, {'status': 'unchanging', 'key': 'key', 'value': 'value'}, {'status': 'added', 'key': 'ops', 'value': 'vops'}]}]}, {'status': 'unchanging', 'key': 'group1', 'value': [{'status': 'changing', 'key': 'baz', 'from': 'bas', 'to': 'bars'}, {'status': 'unchanging', 'key': 'foo', 'value': 'bar'}, {'status': 'changing', 'key': 'nest', 'from': {'key': 'value'}, 'to': 'str'}]}, {'status': 'removed', 'key': 'group2', 'value': {'abc': 12345, 'deep': {'id': 45}}}, {'status': 'added', 'key': 'group3', 'value': {'deep': {'id': {'number': 45}}, 'fee': 100500}}]

def chek_complex(data):
    if isinstance(data, list):
        return f"[complex value]"
    return data


# Ниже представлена реализация форматера plain через основную функцию flatten, в которой предполагается использование вспомогательных
# функций get_path и chek_complex для функционального отображения пути, а так же конкретики изменений сравниваемых файлов.
def flatten(data):
    row = []

    def inner(data):
        for value in data:
            if isinstance(value[2], list):
                inner(value[2])
            if value[0] in '+':
                row.append(f"Property {get_path(data, value[2])} was added with value: {chek_complex(value[2])}")
            elif value[0] in '-':
                row.append(f"Property {get_path(data, value[2])} was removed")
            # Где-то тут будет реализация последнего условия - 'was update...'
        return '\n'.join(row)

    return inner

#print(flatten(data)(data))
