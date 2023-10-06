from gendiff.build_diff import keys
from gendiff.formatter.stylish import make_stylish


def apply_format(diff, dict1, dict2, formatter):
    _, first_level_keys = keys(dict1, dict2)
    if formatter == 'stylish':
        return make_stylish(first_level_keys, diff)
