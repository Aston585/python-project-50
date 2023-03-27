from gendiff.gendiff import generate_diff
file1_json = './tests/fixtures/file1.json'
file2_json = './tests/fixtures/file2.json'
file1_yaml = './tests/fixtures/file1.yml'
file2_yaml = './tests/fixtures/file2.yml'

def open_correct_view():
    with open('./tests/fixtures/right_stylish_format.txt') as stylish:
        right_stylish = stylish.read()
    with open('./tests/fixtures/right_plain_format.txt') as plain:
        right_plain = plain.read()
    return right_stylish, right_plain


def test_generate_diff_json():
    assert open_correct_view()[0] == generate_diff(file1, file2)


def test_generate_diff_yaml():
    assert open_correct_view()[1] == generate_diff(file1, file2)
