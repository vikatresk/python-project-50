import json
import yaml
import os


def load_file(file_path):
    with open(file_path) as file:
        data = file.read()
        _, extnsn = os.path.splitext(file_path)
    return parse_data(data, extnsn)


def parse_data(data, extension):
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(data)
    elif extension == '.json':
        return json.loads(data)
    else:
        raise Exception('Invalid format!')
