from argparse import ArgumentParser


def parse_args():
    parser = ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.add_argument(
        '-f',
        '--format',
        metavar='FORMAT',
        help='set format of output',
    )
    return parser.parse_args()
