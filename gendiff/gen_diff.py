import json


def generate_diff(first_file, second_file):
    file1 = json.load(open(first_file))
    file2 = json.load(open(second_file))
    keys = sorted(set(file1.keys() | set(file2.keys())))
    result = ''
    for key in keys:
        if file1.get(key) is None:
            result += f"+ {key}: {file2[key]}\n"
        elif file1.get(key) is not None and file2.get(key) is None:
            result += f"- {key}: {file1[key]}\n"
        elif file1.get(key) == file2.get(key):
            result += f"  {key}: {file1[key]}\n"
        else:
            result += f"- {key}: {file1[key]}\n+ {key}: {file2[key]}\n"
    diff = result.strip().lower()
    return "{\n" + diff + "\n}"