#!/usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.gen_diff import generate_diff


def main():
    args = parse_args()
    difference = generate_diff(args.first_file, args.second_file, args.format)
    print(difference)


if __name__ == '__main__':
    main()
