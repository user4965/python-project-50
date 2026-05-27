import itertools
from typing import Any


def format_value(value: Any, depth: int) -> str:
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return 'null'

    if not isinstance(value, dict):
        return str(value)

    deep_indent_size = depth + 4
    deep_indent = ' ' * deep_indent_size
    current_indent = ' ' * depth
    lines = []
    for key, val in value.items():
        formatted_value = format_value(val, deep_indent_size)
        lines.append(f'{deep_indent}{key}: {formatted_value}')
    result = itertools.chain(["{"], lines, [current_indent + "}"])
    return '\n'.join(result)


def format_stylish(diff: list[dict[str, Any]]) -> str:
    def iter_(nodes: list[dict[str, Any]], depth: int) -> str:
        current_indent = ' ' * depth
        deep_indent_size = depth + 4
        deep_indent = ' ' * deep_indent_size
        sign_indent = ' ' * (deep_indent_size - 2)
        lines = []

        for node in nodes:
            status = node['status']

            if status == 'removed':
                key = node['key']
                value = format_value(node['value'], deep_indent_size)
                lines.append(f"{sign_indent}- {key}: {value}")

            elif status == 'added':
                key = node['key']
                value = format_value(node['value'], deep_indent_size)
                lines.append(f"{sign_indent}+ {key}: {value}")

            elif status == 'changed':
                key = node['key']
                old_value = format_value(node['old_value'], deep_indent_size)
                new_value = format_value(node['new_value'], deep_indent_size)
                lines.append(f"{sign_indent}- {key}: {old_value}")
                lines.append(f"{sign_indent}+ {key}: {new_value}")

            elif status == 'unchanged':
                key = node['key']
                value = format_value(node['value'], deep_indent_size)
                lines.append(f"{deep_indent}{key}: {value}")

            elif status == 'nested':
                key = node['key']
                children = node['children']
                formatted_children = iter_(children, deep_indent_size)
                lines.append(f"{deep_indent}{key}: {formatted_children}")

        result = itertools.chain(["{"], lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(diff, 0)
