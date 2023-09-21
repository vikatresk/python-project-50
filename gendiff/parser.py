import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows differences."
        )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args