from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make_json


def apply_format(data, formatter='stylish'):
    if formatter == 'plain':
        return make_plain(data)
    if formatter == 'json':
        return make_json(data)
    return make_stylish(data)
