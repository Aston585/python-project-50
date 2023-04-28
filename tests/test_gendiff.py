from gendiff.gendiff import generate_diff

file1_json = './tests/fixtures/file1.json'
file2_json = './tests/fixtures/file2.json'
file1_yml = './tests/fixtures/file1.yml'
file2_yaml = './tests/fixtures/file2.yaml'


def open_correct_view_stylish():
    with open('./tests/fixtures/right_stylish_format.txt') as stylish:
        return stylish.read()


def open_correct_view_plain():
    with open('./tests/fixtures/right_plain_format.txt') as plain:
        return plain.read()


def open_correct_view_json():
    with open('./tests/fixtures/right_json_format.txt') as json:
        return json.read()


def test_generate_diff_stylish():
    assert open_correct_view_stylish() == generate_diff(file1_json, file2_yaml)


def test_generate_diff_plain():
    assert open_correct_view_plain() == generate_diff(file1_yml, file2_json, format_name='plain')


def test_generate_diff_json_format():
    assert open_correct_view_json() == generate_diff(file1_yml, file2_yaml, format_name='json')
