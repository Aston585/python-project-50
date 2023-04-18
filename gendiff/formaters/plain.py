# Погружение в контекст вопроса:

# Переменная data содержит выходные данные из ядра вычислителя отличий,
# которые являются входными данными для функции flatten, которая в свою очередь выполняет требуемую
# функциональность форматера plain.

data = [(' ', 'common', [('+', 'follow', False), (' ', 'setting1', 'Value 1'), ('-', 'setting2', 200), ('-', 'setting3', True),
                         ('+', 'setting3', 'null'), ('+', 'setting4', 'blah blah'), ('+', 'setting5', [(' ', 'key5', 'value5')]),
                         (' ', 'setting6', [(' ', 'doge', [('-', 'wow', ''), ('+', 'wow', 'so much')]), (' ', 'key', 'value'),
                         ('+', 'ops', 'vops')])]), (' ', 'group1', [('-', 'baz', 'bas'), ('+', 'baz', 'bars'), (' ', 'foo', 'bar'),
                         ('-', 'nest', [(' ', 'key', 'value')]), ('+', 'nest', 'str')]), ('-', 'group2', [(' ', 'abc', 12345),
                         (' ', 'deep', [(' ', 'id', 45)])]), ('+', 'group3', [(' ', 'deep', [(' ', 'id', [(' ', 'number', 45)])]),
                         (' ', 'fee', 100500)])]





# С помощью вспомогательной функции get_path я планирую получать путь к требуемуему значению 'key', которое
# передается из основной функции flatten, как аргумент функции get_path.
# Например, если нужно будет построить путь до значения 'baz', то функция должна вернуть ['group1', 'baz'].

# Однако, на данный момент вывод получается таким: ['common', 'setting6', 'doge', 'group1', 'baz'].
#
# ***Вопрос***
# Как сделать чтобы, если искомое значение 'key' не было найдено на текущем уровне итерации, то при возврате на предыдущий
# уровень значения 'пустых' уровней, записываемые в переменную path, удалялись?
# В данном случае 'пустые' уровни это: 'common', 'setting6', 'doge'
key = 'baz'


def get_path(data, key):
    path = []

    def inner(data, key):
        for value in data:
            if (isinstance(value[2], list)) and (value[0] in " "):
                path.append(value[1])
                inner(value[2], key)
            if value[1] == key:
                path.append(value[1])
                return path
        return path

    return inner

print(get_path(data, key)(data, key))
# ['common', 'setting6', 'doge', 'group1', 'baz']


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
