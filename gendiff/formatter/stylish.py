STATUS = {
    'unchanged': "  ",
    'added': "+ ",
    'deleted': "- "
}
REPLACER = " "


def to_str(value, spaces_count=2):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        indent = REPLACER * (spaces_count + 4)
        lines = []
        for k, v in value.items():
            str_value = to_str(v, spaces_count + 4)
            lines.append(f"{indent}{STATUS['unchanged']}{k}: {str_value}")
        result = '\n'.join(lines)
        end_indent = REPLACER * (spaces_count + 2)
        return f"{{\n{result}\n{end_indent}}}"
    return f"{value}"


def make_stylish(data, spaces_count=2):
    lines = []
    indent = REPLACER * spaces_count
    for diff in data:
        if 'status' in diff:
            status = diff['status']
            if status == 'changed':
                value1 = to_str(diff['value1'], spaces_count)
                value2 = to_str(diff['value2'], spaces_count)
                new_key1 = STATUS['deleted'] + diff['key']
                new_key2 = STATUS['added'] + diff['key']
                lines.append(
                    f'{indent}{new_key1}: {value1}')
                lines.append(
                    f'{indent}{new_key2}: {value2}')
            elif status == 'parent':
                children = make_stylish(diff['value'], spaces_count + 4)
                new_key = STATUS['unchanged'] + diff['key']
                lines.append(
                    f'{indent}{new_key}: {children}')
            else:
                value = to_str(diff['value'], spaces_count)
                new_key = STATUS[diff['status']] + diff['key']
                lines.append(
                    f'{indent}{new_key}: {value}')
    stylish_result = '\n'.join(lines)
    end_indent = REPLACER * (spaces_count - 2)
    return f"{{\n{stylish_result}\n{end_indent}}}"
