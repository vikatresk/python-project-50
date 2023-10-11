INDENT_COUNT = 4
REPLACER = ' '


def make_stylish(data):
    return make_diff(data, depth=1)


def make_diff(current_data, depth):
    if not isinstance(current_data, (list, dict)):
        return str(current_data)
    lines = make_lines(current_data, depth)
    return '\n'.join(lines)


def make_lines(current_data, depth):
    indent = REPLACER * INDENT_COUNT * depth
    closing_indent = REPLACER * INDENT_COUNT * (depth - 1)
    lines = []

    if isinstance(current_data, dict):
        for k, v in current_data.items():
            lines.append(f'{indent}{k}: {make_diff(v, depth=depth + 1)}')
    for diff in current_data:
        add_lines(diff, depth, lines)

    result = ['{'] + lines + [closing_indent + '}']
    return result


def add_lines(diff, depth, lines):
    status = get_status(diff)
    if status == 'deleted':
        indent = REPLACER * ((INDENT_COUNT * depth) - 2)
        value = to_str(diff['value'])
        key = '- ' + diff['key']
        lines.append(
            f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
        )
    elif status == 'added':
        indent = REPLACER * ((INDENT_COUNT * depth) - 2)
        value = to_str(diff['value'])
        key = '+ ' + diff['key']
        lines.append(
            f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
        )
    elif status == 'unchanged':
        indent = REPLACER * INDENT_COUNT * depth
        value = to_str(diff['value'])
        key = diff['key']
        lines.append(
            f'{indent}{key}: {make_diff(value, depth=depth + 1)}'
        )
    elif status == 'changed':
        indent = REPLACER * ((INDENT_COUNT * depth) - 2)
        value1 = to_str(diff['value1'])
        value2 = to_str(diff['value2'])
        key1 = '- ' + diff['key']
        key2 = '+ ' + diff['key']
        lines.append(
            f'{indent}{key1}: {make_diff(value1, depth=depth + 1)}'
        )
        lines.append(
            f'{indent}{key2}: {make_diff(value2, depth=depth + 1)}'
        )
    elif status == 'parent':
        indent = REPLACER * INDENT_COUNT * depth
        children = to_str(diff['children'])
        key = diff['key']
        lines.append(
            f'{indent}{key}: {make_diff(children, depth=depth + 1)}'
        )
    return lines


def get_status(diff):
    if 'status' in diff:
        return diff['status']


def to_str(value):
    if value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for v in value.values():
            v = to_str(v)
    return value
