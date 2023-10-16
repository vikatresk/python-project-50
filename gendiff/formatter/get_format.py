from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain
from gendiff.formatter.json import make_json


def apply_format(data, formatter):
    if formatter == 'stylish':
        return make_stylish(data)
    elif formatter == 'json':
        return make_json(data)
    elif formatter == 'plain':
        return make_plain(data)
    else:
        raise Exception('Invalid formatter!')
