from argparse import Namespace
from unique_symbols import unique_characters, get_parser, cli
import pytest
from unittest.mock import patch, Mock, mock_open
import sys


@pytest.mark.parametrize("text, expected_result", [('qwweerrt1', 3), ('timer 123', 8), ('', 0),
                                                   ('xxzzccvvbbmmmssss', 0), ('cooperation', 8),
                                                   ('@@@#qqwer', 4), ('######', 0)])
def test_unique_characters(text, expected_result):
    assert unique_characters(text) == expected_result


def test_get_parser():
    test_args = ['fake_unique_symbols.py', '-f', 'fake/path/for/tests']
    with patch.object(sys, 'argv', test_args):
        setup = get_parser()
        assert str(setup) == "ArgumentParser(prog='fake_unique_symbols.py', usage=None, " \
                             "description='Shows uniques symbols in string or in text file', " \
                             "formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', " \
                             "add_help=True)"


@pytest.mark.parametrize("parsed_data, expected_result", [(Namespace(file=None, string='poiuy'), '5\n'),
                                                          (Namespace(file='its/fake/path', string=None),
                                                           "No such file or directory: its/fake/path\n")])
@patch('unique_symbols.unique_symbols.get_parser')
def test_cli_without_reading_file(mock_get_parser, parsed_data, expected_result, capsys):
    mock_get_parser.return_value = Mock(parse_args=Mock(return_value=parsed_data))
    cli()
    out, err = capsys.readouterr()
    assert out == expected_result


@pytest.mark.parametrize("parsed_data, expected_output", [(Namespace(file='its/fake/path', string=None), '6\n'),
                                                         (Namespace(file='its/fake/path', string='zxcvbnmrtg'), '6\n')])
@patch('unique_symbols.unique_symbols.get_parser')
def test_cli_with_reading_file(mock_get_parser, parsed_data, expected_output, capsys):
    mock_file_content = "text from file"
    mock_get_parser.return_value = Mock(parse_args=Mock(return_value=parsed_data))
    with patch('builtins.open', mock_open(read_data=mock_file_content)) as _file:
        cli()
        out, err = capsys.readouterr()
        assert out == expected_output


if __name__ == '__main__':
    pytest.main()
