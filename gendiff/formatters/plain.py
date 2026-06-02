from typing import Any


def format_value(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    if isinstance(value, dict):
        return "[complex value]"
    return str(value)


def format_plain(diff: list[dict[str, Any]]) -> str:
    def _iter(
        nodes: list[dict[str, Any]],
        path: list[str],
    ) -> list[str]:
        lines = []

        for node in nodes:
            status = node["status"]

            if status == "removed":
                key = node["key"]
                current_path = path + [key]
                property_name = ".".join(current_path)
                lines.append(
                    f"Property '{property_name}' was removed"
                )

            elif status == "added":
                key = node["key"]
                value = format_value(node["value"])
                current_path = path + [key]
                property_name = ".".join(current_path)
                lines.append(
                    f"Property '{property_name}' was added with value: {value}"
                )

            elif status == "changed":
                key = node["key"]
                old_value = format_value(node["old_value"])
                new_value = format_value(node["new_value"])
                current_path = path + [key]
                property_name = ".".join(current_path)
                lines.append(
                    f"Property '{property_name}' was updated. "
                    f"From {old_value} to {new_value}"
                )

            elif status == "unchanged":
                pass

            elif status == "nested":
                key = node["key"]
                children = node["children"]
                current_path = path + [key]
                lines.extend(_iter(children, current_path))

        return lines

    result = _iter(diff, [])
    return "\n".join(result)