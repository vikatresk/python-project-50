import pytest
from gendiff.gen_diff import generate_diff


FLAT_JSON1 = './tests/fixtures/input/flat1.json'
FLAT_JSON2 = './tests/fixtures/input/flat2.json'
FLAT_YML1 = './tests/fixtures/input/flat1.yml'
FLAT_YML2 = './tests/fixtures/input/flat2.yml'
NESTED_JSON1 = './tests/fixtures/input/nested1.json'
NESTED_JSON2 = './tests/fixtures/input/nested2.json'
NESTED_YML1 = './tests/fixtures/input/nested1.yml'
NESTED_YML2 = './tests/fixtures/input/nested2.yml'

STYLISH_FORMAT_JSON = './tests/fixtures/output/stylish_format_json.txt'
STYLISH_FORMAT_YML = './tests/fixtures/output/stylish_format_yml.txt'
STYLISH_NESTED = './tests/fixtures/output/stylish_format_nested.txt'
PLAIN_JSON = './tests/fixtures/output/plain_format_json.txt'
PLAIN_YML = './tests/fixtures/output/plain_format_yml.txt'
PLAIN_NESTED = './tests/fixtures/output/plain_format_nested.txt'
JSON_FORMAT_JSON = './tests/fixtures/output/json_format_json.txt'
JSON_FORMAT_YML = './tests/fixtures/output/json_format_yml.txt'
JSON_FORMAT_NESTED = './tests/fixtures/output/json_format_nested.txt'


@pytest.mark.parametrize('input1, input2, output, format_', [
    (FLAT_JSON1, FLAT_JSON2, STYLISH_FORMAT_JSON, 'stylish'),
    (FLAT_YML1, FLAT_YML2, STYLISH_FORMAT_YML, 'stylish'),
    (NESTED_JSON1, NESTED_JSON2, STYLISH_NESTED, 'stylish'),
    (NESTED_YML1, NESTED_YML2, STYLISH_NESTED, 'stylish'),
    (FLAT_JSON1, FLAT_JSON2, PLAIN_JSON, 'plain'),
    (FLAT_YML1, FLAT_YML2, PLAIN_YML, 'plain'),
    (NESTED_JSON1, NESTED_JSON2, PLAIN_NESTED, 'plain'),
    (NESTED_YML1, NESTED_YML2, PLAIN_NESTED, 'plain'),
    (FLAT_JSON1, FLAT_JSON2, JSON_FORMAT_JSON, 'json'),
    (FLAT_YML1, FLAT_YML2, JSON_FORMAT_YML, 'json'),
    (NESTED_JSON1, NESTED_JSON2, JSON_FORMAT_NESTED, 'json'),
    (NESTED_YML1, NESTED_YML2, JSON_FORMAT_NESTED, 'json'),

])
def test_generate_diff(input1, input2, output, format_):
    with open(output) as file:
        expected_diff = file.read()
    assert generate_diff(input1, input2, format_) == expected_diff
