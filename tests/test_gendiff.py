from gendiff.app import generate_diff
from itertools import cycle, repeat
import pytest

first_version_files = (
    './tests/fixtures/file1.json',
    './tests/fixtures/file1.yaml',
)

second_version_files = (
    './tests/fixtures/file2.json',
    './tests/fixtures/file2.yaml',
)

pass_correct_outputs = (
    './tests/fixtures/right_stylish_format.txt',
    './tests/fixtures/right_plain_format.txt',
    './tests/fixtures/right_json_format.txt'
)

correct_output_stylish_format = './tests/fixtures/right_stylish_format.txt'
correct_output_plain_format = './tests/fixtures/right_plain_format.txt'
correct_output_json_format = './tests/fixtures/right_json_format.txt'


stylish_format_output = 'stylish'
plain_format_output = 'plain'
json_format_output = 'json'


@pytest.mark.parametrize(
    'file1, file2, correct_outputs, format_output',
    [
        (file1, file2, correct_outputs, format_output)
        for (file1, file2, correct_outputs, format_output) in zip(
            cycle(first_version_files),
            cycle(second_version_files),
            [
                *repeat(correct_output_stylish_format, 2),
                *repeat(correct_output_plain_format, 2),
                *repeat(correct_output_json_format, 2),
            ],
            [
                *repeat(stylish_format_output, 2),
                *repeat(plain_format_output, 2),
                *repeat(json_format_output, 2),
            ]
        )

    ]
)
def test_generate_diff(file1, file2, correct_outputs, format_output):
    with open(correct_outputs) as f:
        expected = f.read()
    eval_result = generate_diff(file1, file2, format_output)
    assert eval_result == expected
