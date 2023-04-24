from gendiff.gendiff import generate_diff

file1_json = './tests/fixtures/file1.json'
file2_json = './tests/fixtures/file2.json'
file1_yaml = './tests/fixtures/file1.yml'
file2_yaml = './tests/fixtures/file2.yml'


def open_correct_view_stylish():
    with open('./tests/fixtures/right_stylish_format.txt') as stylish:
        return stylish.read()


def open_correct_view_plain():
    with open('./tests/fixtures/right_plain_format.txt') as plain:
        return plain.read()


def test_generate_diff_stylish_json():
    assert open_correct_view_stylish() == generate_diff(file1_json, file2_json)


def test_generate_diff_stylish_yaml():
    assert open_correct_view_stylish() == generate_diff(file1_yaml, file2_yaml)


def test_generate_diff_plain_json():
    assert open_correct_view_plain() == generate_diff(file1_json, file2_json, format_name='plain')


#def test_generate_diff_plain_yaml():
    #assert open_correct_view_plain() == generate_diff(file1_yaml, file2_yaml, format_name='plain')
