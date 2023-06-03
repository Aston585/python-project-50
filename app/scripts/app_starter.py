#!/usr/bin/env python3


from app.parser_cli import get_parser
from app.gendiff import generate_diff


def main():
    args = get_parser().parse_args()
    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))


if __name__ == '__main__':
    main()
