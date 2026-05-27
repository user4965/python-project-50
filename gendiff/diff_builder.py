from typing import Any

REMOVED = 'removed'
ADDED = 'added'
NESTED = 'nested'
CHANGED = 'changed'
UNCHANGED = 'unchanged'


def build_diff(
    dict1: dict[str, Any],
    dict2: dict[str, Any],
) -> list[dict[str, Any]]:
    sorted_keys = sorted(dict1.keys() | dict2.keys())
    result: list[dict[str, Any]] = []

    for key in sorted_keys:
        if key in dict1 and key not in dict2:
            result.append({'key': key, 'status': REMOVED, 'value': dict1[key]})
        elif key in dict2 and key not in dict1:
            result.append({'key': key, 'status': ADDED, 'value': dict2[key]})
        elif (
            key in dict1
            and key in dict2
            and isinstance(dict1[key], dict)
            and isinstance(dict2[key], dict)
        ):
            children = build_diff(dict1[key], dict2[key])
            result.append({'key': key, 'status': NESTED, 'children': children})
        elif key in dict1 and key in dict2 and dict1[key] != dict2[key]:
            result.append(
                {'key': key,
                 'status': CHANGED,
                 'old_value': dict1[key],
                 'new_value': dict2[key]})
        else:
            result.append(
                {'key': key,
                 'status': UNCHANGED,
                 'value': dict1[key]})

    return result
