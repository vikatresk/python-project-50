def compare_dicts(dict1, dict2):
    keys = dict1.keys() | dict2.keys()
    diff = []
    for key in sorted(keys):
        if key in dict1 and key not in dict2:
            diff.append({
                'status': 'deleted',
                'key': key,
                'value': dict1[key]
            })
        elif key in dict2 and key not in dict1:
            diff.append({
                'status': 'added',
                'key': key,
                'value': dict2[key]
            })
        elif dict1[key] == dict2[key]:
            diff.append({
                'status': 'unchanged',
                'key': key,
                'value': dict1[key]
            })
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            diff.append({
                'status': 'parent',
                'key': key,
                'children': compare_dicts(dict1[key], dict2[key])
            })
        else:
            diff.append({
                'status': 'changed',
                'key': key,
                'value1': dict1[key],
                'value2': dict2[key]
            })
    return diff
