import json
from pathlib import Path
from typing import Any

import yaml


def parse_file(path: str | Path) -> dict[str, Any]:
    path = Path(path)
    with open(path) as file:
        if path.suffix == '.json':
            return json.load(file)
        elif path.suffix == '.yaml' or path.suffix == '.yml':
            return yaml.safe_load(file)
        raise ValueError("Wrong file format")
