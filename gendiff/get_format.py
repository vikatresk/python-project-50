from gendiff.formatter.stylish import make_stylish


def apply_format(data, formatter):
    if formatter == 'stylish':
        return make_stylish(data)
