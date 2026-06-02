import json
from pathlib import Path
from typing import Any

import yaml


def parse_file(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    suffix = path.suffix

    with open(path) as file:
        if suffix == '.json':
            return json.load(file)
        elif suffix == '.yaml' or suffix == '.yml':
            return yaml.safe_load(file)
        raise ValueError("Wrong file format")
