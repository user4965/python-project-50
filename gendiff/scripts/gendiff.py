from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument('first_file', type=str, help='Path to the first file')
    parser.add_argument('second_file', type=str, help='Path to the second file')
    parser.parse_args()

if __name__ == '__main__':
    main()
