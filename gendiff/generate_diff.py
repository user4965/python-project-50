import json


def load_json(path):
    with open(path) as file:
        return json.load(file)


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    dict1 = load_json(file_path1)
    dict2 = load_json(file_path2)
    sorted_keys = sorted(dict1.keys() | dict2.keys())
    result = []
    for key in sorted_keys:
        if key in dict1 and key not in dict2:
            result.append(f" - {key}: {format_value(dict1[key])}")
        elif key in dict2 and key not in dict1:
            result.append(f" + {key}: {format_value(dict2[key])}")
        elif key in dict1 and key in dict2 and dict1[key] != dict2[key]:
            result.append(f" - {key}: {format_value(dict1[key])}")
            result.append(f" + {key}: {format_value(dict2[key])}")
        else:
            result.append(f"   {key}: {format_value(dict1[key])}")
    joined_str = '\n'.join(result)
    return f"{{\n{joined_str}\n}}"
