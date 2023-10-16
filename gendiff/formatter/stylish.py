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


def make_stylish(data, replacer=' ', spaces_count=4):  # noqa: C901
    def collect(current_value, depth):
        if not isinstance(current_value, (list, dict)):
            return str(current_value)
        indent_size1 = depth * spaces_count + 2
        indent_size2 = depth * spaces_count + 4
        indent1 = replacer * indent_size1
        indent2 = replacer * indent_size2
        current_indent = replacer * (depth * spaces_count)
        lines = []
        if isinstance(current_value, dict):
            for k, v in current_value.items():
                lines.append(f'{indent2}{k}: {collect(v, depth + 1)}')
        for diff in current_value:
            if 'status' in diff:
                status = diff['status']
                if status == 'deleted':
                    value = to_str(diff['value'])
                    new_key = '- ' + diff['key']
                    lines.append(
                        f'{indent1}{new_key}: {collect(value, depth + 1)}'
                    )
                elif status == 'added':
                    value = to_str(diff['value'])
                    new_key = '+ ' + diff['key']
                    lines.append(
                        f'{indent1}{new_key}: {collect(value, depth + 1)}'
                    )
                elif status == 'unchanged':
                    value = to_str(diff['value'])
                    new_key = '  ' + diff['key']
                    lines.append(
                        f'{indent1}{new_key}: {collect(value, depth + 1)}'
                    )
                elif status == 'changed':
                    value1 = to_str(diff['value1'])
                    value2 = to_str(diff['value2'])
                    new_key1 = '- ' + diff['key']
                    new_key2 = '+ ' + diff['key']
                    lines.append(
                        f'{indent1}{new_key1}: {collect(value1, depth + 1)}'
                    )
                    lines.append(
                        f'{indent1}{new_key2}: {collect(value2, depth + 1)}'
                    )
                elif status == 'parent':
                    child = to_str(diff['value'])
                    new_key = '  ' + diff['key']
                    lines.append(
                        f'{indent1}{new_key}: {collect(child, depth + 1)}'
                    )
            else:
                pass
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return collect(data, 0)
