#from itertools import chain
#from gendiff.formaters.normalize import normalize_value

data = [(' ', 'common', [('+', 'follow', False), (' ', 'setting1', 'Value 1'), ('-', 'setting2', 200), ('-', 'setting3', True),
                         ('+', 'setting3', 'null'), ('+', 'setting4', 'blah blah'), ('+', 'setting5', [(' ', 'key5', 'value5')]),
                         (' ', 'setting6', [(' ', 'doge', [('-', 'wow', ''), ('+', 'wow', 'so much')]), (' ', 'key', 'value'),
                         ('+', 'ops', 'vops')])]), (' ', 'group1', [('-', 'baz', 'bas'), ('+', 'baz', 'bars'), (' ', 'foo', 'bar'),
                         ('-', 'nest', [(' ', 'key', 'value')]), ('+', 'nest', 'str')]), ('-', 'group2', [(' ', 'abc', 12345),
                         (' ', 'deep', [(' ', 'id', 45)])]), ('+', 'group3', [(' ', 'deep', [(' ', 'id', [(' ', 'number', 45)])]),
                         (' ', 'fee', 100500)])]


path = []
key = 'setting2'

def get_path(data, key):
    for value in data:
        if (isinstance(value[2], list)) and (value[0] in " "):
            path.append(value[1])
            get_path(value[2], key)
        if value[1] == key:
            path.append(value[1])
            return path
        print(path)
    return path


#print(get_path(data, key))


def chek_complex(data):
    if isinstance(data, list):
        return f"[complex value]"
    return data


def flatten(data):
    row = []

    def inner(data):
        for value in data:
            #path.append(value[1])
            if isinstance(value[2], list):

                inner(value[2])
            if value[0] in '+':
                row.append(f"Property 'path' was added with value: {chek_complex(value[2])}")
            elif value[0] in '-':
                row.append(f"Property 'path' was removed ('{value[1]}')")
        return '\n'.join(row)

    return inner

#print(flatten(data)(data))
