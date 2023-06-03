import argparse

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        choices=(STYLISH, PLAIN, JSON),
                        default=STYLISH,
                        help='set format of output: plain or json'
                             ' (default: stylish)')
    return parser
