import json
from gendiff.cli import parse_args


def main():
    args = parse_args()

    dict1 = load_json(args.first_file)
    dict2 = load_json(args.second_file)

    print(dict1)
    print(dict2)


def load_json(path):
    with open(path) as file:
        return json.load(file)


if __name__ == '__main__':
    main()
