import itertools


def to_str(value):
    if value in (False, True):
        value = str(value).lower()
    elif value is None:
        value = 'null'
    elif isinstance(value, dict):
        for k, v in value.items():
            v = to_str(v)
    return value


STATUS = {
    'unchanged': "  ",
    'added': "+ ",
    'deleted': "- "
}


def make_stylish(data, replacer=' ', spaces_count=4):  # noqa c901
    def collect(current_value, depth):
        if not isinstance(current_value, (list, dict)):
            return str(current_value)
        first_line_indent = replacer * (depth * spaces_count + 2)
        last_line_indent = replacer * (depth * spaces_count + 4)
        curr_line_indent = replacer * (depth * spaces_count)
        lines = []
        if isinstance(current_value, dict):
            for k, v in current_value.items():
                lines.append(f'{last_line_indent}{k}: '
                             f'{collect(v, depth + 1)}')
        for diff in current_value:
            if 'status' in diff:
                status = diff['status']
                if status == 'changed':
                    value1 = to_str(diff['value1'])
                    value2 = to_str(diff['value2'])
                    new_key1 = '- ' + diff['key']
                    new_key2 = '+ ' + diff['key']
                    lines.append(
                        f'{first_line_indent}{new_key1}: '
                        f'{collect(value1, depth + 1)}')
                    lines.append(
                        f'{first_line_indent}{new_key2}: '
                        f'{collect(value2, depth + 1)}')
                elif status == 'parent':
                    child = to_str(diff['value'])
                    new_key = '  ' + diff['key']
                    lines.append(
                        f'{first_line_indent}{new_key}: '
                        f'{collect(child, depth + 1)}')
                else:
                    value = to_str(diff['value'])
                    new_key = STATUS[diff['status']] + diff['key']
                    lines.append(
                        f'{first_line_indent}{new_key}: '
                        f'{collect(value, depth + 1)}')

        result = itertools.chain("{", lines, [curr_line_indent + "}"])
        return '\n'.join(result)
    return collect(data, 0)
