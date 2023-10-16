import os.path
from os.path import dirname, abspath
import pytest
from gendiff.gen_diff import generate_diff


INPUT_PATH = os.path.join(f'{dirname(abspath(__file__))}', 'fixtures/input')
OUTPUT_PATH = os.path.join(f'{dirname(abspath(__file__))}', 'fixtures/output')


def get_input_path(file):
    return os.path.join(INPUT_PATH, file)


def get_output_path(file):
    return os.path.join(OUTPUT_PATH, file)


@pytest.mark.parametrize('input1, input2, output, format_', [
    ('flat1.json', 'flat2.json', 'stylish_format_json.txt', 'stylish'),
    ('flat1.yml', 'flat2.yml', 'stylish_format_yml.txt', 'stylish'),
    ('nested1.json', 'nested2.json', 'stylish_format_nested.txt', 'stylish'),
    ('nested1.yml', 'nested2.yml', 'stylish_format_nested.txt', 'stylish'),
    ('flat1.json', 'flat2.json', 'plain_format_json.txt', 'plain'),
    ('flat1.yml', 'flat2.yml', 'plain_format_yml.txt', 'plain'),
    ('nested1.json', 'nested2.json', 'plain_format_nested.txt', 'plain'),
    ('nested1.yml', 'nested2.yml', 'plain_format_nested.txt', 'plain'),
    ('flat1.json', 'flat2.json', 'json_format_json.txt', 'json'),
    ('flat1.yml', 'flat2.yml', 'json_format_yml.txt', 'json'),
    ('nested1.json', 'nested2.json', 'json_format_nested.txt', 'json'),
    ('nested1.yml', 'nested2.yml', 'json_format_nested.txt', 'json'),
])
def test_generate_diff(input1, input2, output, format_):
    file_1 = get_input_path(input1)
    file_2 = get_input_path(input2)
    with open(get_output_path(output)) as file:
        expected_diff = file.read()
        assert generate_diff(file_1, file_2, format_) == expected_diff
