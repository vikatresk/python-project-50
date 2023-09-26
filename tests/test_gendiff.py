from gendiff import generate_diff


def test_json_flat_diff():
    file1 = './tests/fixtures/input/flat1.json'
    file2 = './tests/fixtures/input/flat2.json'
    with open('./tests/fixtures/output/result_flat_json.txt') as file:
        expected = file.read()
        diff = generate_diff(file1, file2)
        assert expected == diff
