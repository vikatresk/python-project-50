import json
import yaml
import os


def get_content(file_path):
    with open(file_path) as file:
        content = file.read()
        _, format = os.path.splitext(file_path)
        return parse(content, format[1:])


def parse(content, format):
    if format in ('yaml', 'yml'):
        return yaml.safe_load(content)
    elif format == 'json':
        return json.loads(content)
    else:
        raise Exception('Invalid format!')
