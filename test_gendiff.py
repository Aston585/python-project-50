from gendiff.gendiff import generate_diff


def test_generate_diff():
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    with open('./tests/fixtures/right.txt') as r:
        right = r.read()
        assert right == generate_diff(file1, file2)
