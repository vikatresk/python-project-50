from gendiff.parse_data import get_content
from gendiff.formatter.get_format import apply_format
from gendiff.build_diff import compare_dicts


def generate_diff(first_file, second_file, formatter='stylish'):
    dict1 = get_content(first_file)
    dict2 = get_content(second_file)
    diff = compare_dicts(dict1, dict2)
    return apply_format(diff, formatter)
