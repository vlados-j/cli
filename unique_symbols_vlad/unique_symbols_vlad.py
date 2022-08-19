from collections import Counter
from functools import lru_cache
import argparse


def get_parser():
    my_parser = argparse.ArgumentParser(description='Shows uniques symbols in string or in text file')

    my_parser.add_argument('-f', '--file', type=str, help='the path to a text file')
    my_parser.add_argument('-s', '--string', type=str, help='an input string')

    return my_parser


def cli():
    parser = get_parser()
    parsers_data = parser.parse_args()
    if parsers_data.file is not None:
        try:
            with open(parsers_data.file, 'r') as file:
                print(unique_characters(file.read()))
        except FileNotFoundError:
            print(f'No such file or directory:', parsers_data.file)
    elif parsers_data.string is not None:
        print(unique_characters(parsers_data.string))
    else:
        parser.print_help()


@lru_cache
def unique_characters(text: str) -> int:
    character_count = Counter(text)
    unique_symbols_list = [key for key, value in character_count.items() if key != ' ' and value == 1]
    return len(unique_symbols_list)


if __name__ == '__main__':
    cli()
