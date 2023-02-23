#!/usr/bin/env python3

import argparse
from gendiff import gendiff


def get_parser():
    parser = argparse.ArgumentParser(
            description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    args = get_parser()
    gendiff.generate_diff(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
