from gendiff.formatter.stylish import make_stylish
from gendiff.formatter.plain import make_plain


def apply_format(data, formatter):
    if formatter == 'stylish':
        return make_stylish(data)
    if formatter == 'plain':
        return make_plain(data)
