from gendiff.gen_diff import generate_diff


def test_json_flat_diff():
    file1 = './tests/fixtures/input/flat1.json'
    file2 = './tests/fixtures/input/flat2.json'
    with open('./tests/fixtures/output/result_flat_json.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff


def test_yml_flat_diff():
    file1 = './tests/fixtures/input/flat1.yml'
    file2 = './tests/fixtures/input/flat2.yml'
    with open('./tests/fixtures/output/result_flat_yml.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff


def test_both_flat_diff():
    file1 = './tests/fixtures/input/flat1.json'
    file2 = './tests/fixtures/input/flat2.yml'
    with open('./tests/fixtures/output/result_flat_yml.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff


def test_nested_yml_stylish():
    file1 = "./tests/fixtures/input/nested1.yml"
    file2 = "./tests/fixtures/input/nested2.yml"
    with open("./tests/fixtures/output/stylish_result_nested.txt") as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff


def test_nested_plain():
    file1 = "./tests/fixtures/input/nested1.yml"
    file2 = "./tests/fixtures/input/nested2.yml"
    with open("./tests/fixtures/output/plain_result_nested.txt") as file:
        expected = file.read()
        diff = generate_diff(file1, file2, 'plain')
        assert expected == diff


def test_nested_in_json_format():
    file1 = "./tests/fixtures/input/nested1.yml"
    file2 = "./tests/fixtures/input/nested2.yml"
    with open("./tests/fixtures/output/json_result_nested.txt") as file:
        expected = file.read()
        diff = generate_diff(file1, file2, 'json')
        assert expected == diff
