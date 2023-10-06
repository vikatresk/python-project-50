from gendiff.parse_data import load_file
from gendiff.get_format import apply_format
from gendiff.build_diff import compare_dicts


def generate_diff(first_file, second_file, formatter='stylish'):
    dict1 = load_file(first_file)
    dict2 = load_file(second_file)
    diff = compare_dicts(dict1, dict2)
    return apply_format(diff, formatter)
