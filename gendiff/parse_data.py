import json
import yaml
import os


def load_file(file_path):
    with open(file_path) as file:
        data = file.read()
        _, extension = os.path.splitext(file_path)
        return parsing_file(data, extension)


def parsing_file(data, extension):
    if extension in ('.yaml', '.yml'):
        return yaml.safe_load(data)
    elif extension == '.json':
        return json.loads(data)
    else:
        raise Exception('Invalid format!')
