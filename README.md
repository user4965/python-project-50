### Hexlet tests and linter status:
[![Python CI](https://github.com/user4965/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/user4965/python-project-50/actions/workflows/pyci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=user4965_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=user4965_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=user4965_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=user4965_python-project-50)

## Gendiff

Compares two configuration files and shows a difference.

Supported input formats:

- JSON
- YAML

Supported output formats:

- stylish, default
- plain
- json

## Usage

```bash
gendiff file1.json file2.json
gendiff --format plain file1.json file2.json
gendiff --format json file1.json file2.json
```

### Demo

Flat JSON
[![asciicast](https://asciinema.org/a/g99PCdvLvxOk6QJi.svg)](https://asciinema.org/a/g99PCdvLvxOk6QJi)

Flat YAML
[![asciicast](https://asciinema.org/a/yxDG1qaZKcLyUjiI.svg)](https://asciinema.org/a/yxDG1qaZKcLyUjiI)

Nested stylish
[![asciicast](https://asciinema.org/a/Un6vbYZxplMRnjYM.svg)](https://asciinema.org/a/Un6vbYZxplMRnjYM)

Plain format
[![asciicast](https://asciinema.org/a/ZAH8yvRSocjQ1ZkL.svg)](https://asciinema.org/a/ZAH8yvRSocjQ1ZkL)

JSON format
[![asciicast](https://asciinema.org/a/o33bEspp6paPmW6B.svg)](https://asciinema.org/a/o33bEspp6paPmW6B)
