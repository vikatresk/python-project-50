from gendiff.gen_diff import generate_diff


def test_json_flat_diff():
    file1 = './tests/fixtures/input/flat1.json'
    file2 = './tests/fixtures/input/flat2.json'
    with open('./tests/fixtures/output/result_flat_json.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff


def test_different_yml_formats_diff():
    file1 = './tests/fixtures/input/flat1.yaml'
    file2 = './tests/fixtures/input/flat2.yml'
    with open('./tests/fixtures/output/result_flat_yaml.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff
