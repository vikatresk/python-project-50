#!/usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.gen_diff import generate_diff


def main():
    args = parse_args()
    first_file = args.first_file
    second_file = args.second_file
    formatter = args.format
    difference = generate_diff(first_file, second_file, formatter)
    print(difference)


if __name__ == '__main__':
    main()
