#!/usr/bin/env python3

from gendiff.parser import get_parser
from gendiff import gendiff


def main():
    args = get_parser()
    print(gendiff.generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
