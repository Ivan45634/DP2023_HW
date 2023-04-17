"""
Unit tests for search_gen.py
"""
import unittest
from unittest.mock import mock_open, patch
from search_gen import read_and_filter


class TestSearchGen(unittest.TestCase):
    """
    Unit tests for search_gen module.
    """

    def setUp(self):
        """Set up test data."""
        self.filename = "test_file.txt"
        self.words = ["rose", "cats"]
        self.data = "The quick brown fox jumps over the lazy dog." \
                    "\nA Rose by any other name would smell as sweet." \
                    "\nIt's raining cats and dogs." \
                    "\nShe sells seashells by the seashore." \
                    "\nAn apple a day keeps " \
                    "the doctor away.\n"

    def test_lines_with_word(self):
        """Test filtering lines with words."""
        with patch("builtins.open",
                   new_callable=mock_open,
                   read_data=self.data) as mock_file:
            exp_output = [
                "A Rose by any other name would smell as sweet.",
                "It's raining cats and dogs."
                ]
            res = list(read_and_filter(self.filename, self.words))
            self.assertEqual(res, exp_output)

    def test_lines_with_word_file_not_found(self):
        """Test handling of file not found error."""
        with patch("builtins.open", side_effect=FileNotFoundError):
            generator = read_and_filter("nonexistent_file.txt", self.words)
            with self.assertRaises(FileNotFoundError):
                for line in generator:
                    pass

    def test_lines_with_word_empty_words_list(self):
        """Test filtering with empty list of search words."""
        with patch("builtins.open", new_callable=mock_open,
                   read_data=self.data):
            expected_output = []
            res = list(read_and_filter(self.filename, []))
            self.assertEqual(res, expected_output)

    def test_lines_with_word_empty_file(self):
        """Test filtering of empty file."""
        with patch("builtins.open", new_callable=mock_open,
                   read_data=""):
            expected_output = []
            res = list(read_and_filter(self.filename, self.words))
            self.assertEqual(res, expected_output)

    def test_lines_with_word_single_word_match(self):
        """Test filtering with single-word search."""
        with patch("builtins.open", new_callable=mock_open,
                   read_data="A Rose by any other name would smell as sweet."):
            expected_output = [
                "A Rose by any other name would smell as sweet."
                ]
            res = list(read_and_filter(self.filename, ["rose"]))
            self.assertEqual(res, expected_output)

    def test_lines_with_word_partial_word_match(self):
        """Test filtering with partial word search."""
        with patch("builtins.open",
                   new_callable=mock_open,
                   read_data=self.data):
            expected_output = []
            res = list(read_and_filter(self.filename, ["ros"]))
            self.assertEqual(res, expected_output)

    def test_read_and_filter_with_file_object(self):
        """Test filtering with file object."""
        expected_result = [
            'Python is awesome',
            'We can use a generator to read and filter big files'
        ]

        file_content = """Python is awesome
            Generators are great too
            We can use a generator to read and filter big files
            This line should be filtered out
            """
        search_words = ["python", "generator"]
        mock_file = mock_open(read_data=file_content)
        mock_file_handle = mock_file.return_value

        with patch('builtins.open', mock_file):
            result = list(read_and_filter(mock_file_handle, search_words))

        self.assertEqual(mock_file.call_count, 0)
        self.assertEqual(result, expected_result)

    def test_read_and_filter_no_match(self):
        """Test filtering with no matches."""
        mock_file = mock_open(read_data=self.data)
        search_words = ['Apples', 'Coconut']
        expected_result = []

        with patch('builtins.open', mock_file):
            result = list(read_and_filter('file.txt', search_words))

        mock_file.assert_called_once_with('file.txt', 'r', encoding='utf-8')
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
