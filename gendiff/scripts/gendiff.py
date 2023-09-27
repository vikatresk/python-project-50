#!/usr/bin/env python3

from gendiff.parser import get_parser
from gendiff.gen_diff import generate_diff


def main():
    args = get_parser()
    first_file = args.first_file
    second_file = args.second_file
    difference = generate_diff(first_file, second_file)
    print(difference)


if __name__ == '__main__':
    main()
