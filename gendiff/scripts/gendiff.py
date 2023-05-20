#!/usr/bin/env python3

from gendiff.parser import get_parser
from gendiff import gendiff


def main():
    args = get_parser().parse_args()
    print(gendiff.generate_diff(args.first_file,
                                args.second_file,
                                args.format))


if __name__ == '__main__':
    main()
