""" This module contains unit tests for the parse_json function."""
import unittest
from unittest.mock import MagicMock, patch
# import coverage
from parse_json import parse_json

# cov = coverage.Coverage()
# cov.start()


class TestParseJson(unittest.TestCase):
    """
    Test case for the parse_json function.
    """

    def test_parse_json(self):
        """
        Test case for the parse_json function.
        """
        # Создаем заглушку для keyword_callback
        keyword_callback_mock = MagicMock()
        # Тестируем функцию
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1'], ['word2'],
                   keyword_callback_mock
                   )
        # Проверяем, что заглушка была вызвана 2 раза
        keyword_callback_mock.assert_called_once_with('word2',
                                                      'key1', 'Word1 word2')

    def test_parse_json_no_required_fields(self):
        """
        Test case for the parse_json function with no required fields.
        """
        # Создаем заглушку для keyword_callback
        keyword_callback_mock = MagicMock()
        # Тестируем функцию без обязательных полей
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   None, ['word2'], keyword_callback_mock)
        # Проверяем, что заглушка была вызвана 2 раза
        keyword_callback_mock.assert_has_calls([
            unittest.mock.call('word2', 'key1', 'Word1 word2'),
            unittest.mock.call('word2', 'key2', 'word2 word3')
        ])

    def test_missing_fields_continue(self):
        """
        Test case for the parse_json function with no required fields.
        """
        # Создаем заглушку для keyword_callback
        keyword_callback_mock = MagicMock()
        # Проверяем функцию на то, что
        # оператор continue был вызван в функции parse_json
        # в случае отсутствия некоторых ключей в json объекте.
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1', 'key2', 'key3'], ['word2'], keyword_callback_mock)
        # Проверяем, что заглушка была вызвана 2 раза
        keyword_callback_mock.assert_has_calls([
            unittest.mock.call('word2', 'key1', 'Word1 word2'),
            unittest.mock.call('word2', 'key2', 'word2 word3')
        ])

    def test_parse_json_no_keywords(self):
        """
        Test case for the parse_json function with no keywords.
        """
        # Создаем заглушку для keyword_callback
        keyword_callback_mock = MagicMock()
        # Тестируем функцию без ключевых слов
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1'], None, keyword_callback_mock)
        # Проверяем, что заглушка не была вызвана
        keyword_callback_mock.assert_not_called()

    def test_parse_json_no_callback(self):
        """
        Test case for the parse_json function with no callback.
        """
        # Тестируем функцию без обработчика ключевых слов
        parse_json('{"key1": "Word1 word2", "key2": "word2 word3"}',
                   ['key1'], ['word2'], None)

    def test_parse_json_with_empty_string(self):
        """
        Test case for the parse_json function with invalid JSON input.
        """
        self.assertIsNone(parse_json('{}'))

    def test_parse_json_invalid_json(self):
        """
        Test case for the parse_json function with invalid JSON input.
        """
        with patch('json.loads') as mock_loads:
            mock_loads.side_effect = ValueError("Invalid JSON")
            with self.assertRaises(ValueError):
                parse_json('{"name": "John", "age": 30}')
            mock_loads.assert_called_once_with('{"name": "John", "age": 30}')

# cov.stop()
# cov.report()
# cov.html_report(directory='./covhtml')


unittest.main()
