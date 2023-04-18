""" This module contains unit tests for the parse_json function."""
import unittest
from unittest.mock import MagicMock, patch
from parse_json import parse_json


class TestParseJson(unittest.TestCase):
    """
    Test case for the parse_json function.
    """

    def test_parse_json(self):
        """
        Test case for the parse_json function.
        """
        keyword_callback_mock = MagicMock()
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1'], ['word2'],
                   keyword_callback_mock
                   )

        keyword_callback_mock.assert_called_once_with('key1', 'word2')

    def test_parse_json_no_required_fields(self):
        """
        Test case for the parse_json function with no required fields.
        """
        keyword_callback_mock = MagicMock()
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   None, ['word2'], keyword_callback_mock)
        keyword_callback_mock.assert_has_calls([
            unittest.mock.call('key1', 'word2'),
            unittest.mock.call('key2', 'word2')
        ])

    def test_missing_fields_continue(self):
        """
        Test case for the parse_json function with no required fields.
        """
        keyword_callback_mock = MagicMock()
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1', 'key2', 'key3'], ['word2'], keyword_callback_mock)
        keyword_callback_mock.assert_has_calls([
            unittest.mock.call('key1', 'word2'),
            unittest.mock.call('key2', 'word2')
        ])

    def test_parse_json_no_keywords(self):
        """
        Test case for the parse_json function with no keywords.
        """
        keyword_callback_mock = MagicMock()
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1'], None, keyword_callback_mock)
        keyword_callback_mock.assert_not_called()

    def test_print(self):
        """
        Test the case when the None value is passed for required_fields.
        """
        with patch('builtins.print') as mock_print:
            parse_json(json_str='{"field1": "value1", "field2": "value2"}',
                       required_fields=None)
            mock_print.assert_called_with(
                "No required fields. Let's check existing keys!"
            )

    def test_return_none(self):
        """
        Test case when the None value is passed for keywords.
        """
        self.assertIsNone(
                parse_json(
                    json_str='{"field1": "value1", "field2": "value2"}',
                    keywords=None
                    )
                )

    def test_keyword_callback_none(self):
        """
        Test case when the None value is passed for keyword_callback.
        """
        with self.assertRaises(TypeError):
            parse_json('{"field1": "value1", "field2": "value2"}',
                       ['field1'], ['value1'], None)

    def test_parse_json_with_whole_word_match(self):
        """
        Test case when a whole word match with keyword in search
        """
        keywords = ["John"]
        json_str = '{"name": "John", "surname": "Johnson"}'
        keyword_callback = MagicMock()
        parse_json(json_str, None, keywords, keyword_callback)
        keyword_callback.assert_called_once_with('name', 'John')

    def test_parse_json_invalid_json(self):
        """
        Test case for the parse_json function with invalid JSON input.
        """
        with patch('json.loads') as mock_loads:
            mock_loads.side_effect = ValueError("Invalid JSON")
            with self.assertRaises(ValueError):
                parse_json('{"name": "John", "age": 30}')
            mock_loads.assert_called_once_with('{"name": "John", "age": 30}')


if __name__ == '__main__':
    unittest.main()
