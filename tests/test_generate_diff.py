from pathlib import Path

from gendiff import generate_diff


def get_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_path(filename).read_text()


def test_generate_diff():
    path1 = get_path("file1.json")
    path2 = get_path("file2.json")
    expected = read_file("expected_flat.txt")

    actual = generate_diff(path1, path2)

    assert actual == expected
