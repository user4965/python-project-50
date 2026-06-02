from pathlib import Path

from gendiff import generate_diff


def get_path(filename: str) -> Path:
    return Path(__file__).parent / "test_data" / filename


def read_file(filename: str) -> str:
    return get_path(filename).read_text().rstrip("\n")


def test_generate_diff_json() -> None:
    path1 = get_path("file1.json")
    path2 = get_path("file2.json")
    expected = read_file("expected_flat.txt")

    actual = generate_diff(path1, path2)

    assert actual == expected


def test_generate_diff_yaml() -> None:
    path1 = get_path("file1.yml")
    path2 = get_path("file2.yml")
    expected = read_file("expected_flat.txt")

    actual = generate_diff(path1, path2)

    assert actual == expected


def test_generate_diff_nested_json() -> None:
    path1 = get_path("nested_file1.json")
    path2 = get_path("nested_file2.json")
    expected = read_file("expected_nested.txt")

    actual = generate_diff(path1, path2, "stylish")

    assert actual == expected


def test_generate_diff_nested_yaml() -> None:
    path1 = get_path("nested_file1.yml")
    path2 = get_path("nested_file2.yml")
    expected = read_file("expected_nested.txt")

    actual = generate_diff(path1, path2, "stylish")

    assert actual == expected


def test_generate_diff_plain_json() -> None:
    path1 = get_path("nested_file1.json")
    path2 = get_path("nested_file2.json")
    expected = read_file("expected_plain.txt")

    actual = generate_diff(path1, path2, "plain")

    assert actual == expected


def test_generate_diff_plain_yaml() -> None:
    path1 = get_path("nested_file1.yml")
    path2 = get_path("nested_file2.yml")
    expected = read_file("expected_plain.txt")

    actual = generate_diff(path1, path2, "plain")

    assert actual == expected


def test_generate_diff_json_format_json() -> None:
    path1 = get_path("nested_file1.json")
    path2 = get_path("nested_file2.json")
    expected = read_file("expected_json.txt")

    actual = generate_diff(path1, path2, "json")

    assert actual == expected


def test_generate_diff_json_format_yaml() -> None:
    path1 = get_path("nested_file1.yml")
    path2 = get_path("nested_file2.yml")
    expected = read_file("expected_json.txt")

    actual = generate_diff(path1, path2, "json")

    assert actual == expected
