from pathlib import Path

from gendiff.core.diff_builder import build_diff
from gendiff.core.parsers import parse_file
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def generate_diff(
    file_path1: str | Path,
    file_path2: str | Path,
    format_name: str = 'stylish',
) -> str:
    dict1 = parse_file(file_path1)
    dict2 = parse_file(file_path2)
    diff = build_diff(dict1, dict2)

    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    if format_name == 'json':
        return format_json(diff)
    raise ValueError('Unknown format')
