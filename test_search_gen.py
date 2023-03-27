import unittest
from unittest.mock import mock_open, patch
from search_gen import lines_with_word


class TestSearchGen(unittest.TestCase):

    def setUp(self):
        self.filename = "test_file.txt"
        self.words = ["rose", "cat"]
        self.data = "The quick brown fox jumps over the lazy dog.\nA Rose by any other name would smell as sweet." \
                    "\nIt's raining cats and dogs.\nShe sells seashells by the seashore.\nAn apple a day keeps " \
                    "the doctor away.\n"

    def test_lines_with_word_with_mock(self):
        with patch("builtins.open", new_callable=mock_open, read_data=self.data) as mock_file:
            expected_output = ["A Rose by any other name would smell as sweet.", "It's raining cats and dogs."]
            self.assertEqual(list(lines_with_word(self.filename, self.words)), expected_output)

    def test_lines_with_word_file_not_found(self):
        with patch("builtins.open", side_effect=FileNotFoundError):
            with self.assertRaises(FileNotFoundError):
                lines_with_word("nonexistent_file.txt", self.words)

    def test_lines_with_word_empty_words_list(self):
        with patch("builtins.open", new_callable=mock_open, read_data=self.data):
            expected_output = []
            self.assertEqual(list(lines_with_word(self.filename, [])), expected_output)

    def test_lines_with_word_empty_file(self):
        with patch("builtins.open", new_callable=mock_open, read_data=""):
            expected_output = []
            self.assertEqual(list(lines_with_word(self.filename, self.words)), expected_output)

    def test_lines_with_word_single_word_match(self):
        with patch("builtins.open", new_callable=mock_open, read_data="A Rose by any other name would smell as sweet."):
            expected_output = ["A Rose by any other name would smell as sweet."]
            self.assertEqual(list(lines_with_word(self.filename, ["rose"])), expected_output)

    def test_lines_with_word_partial_word_match(self):
        with patch("builtins.open", new_callable=mock_open, read_data=self.data):
            expected_output = []
            self.assertEqual(list(lines_with_word(self.filename, ["ros"])), expected_output)

if __name__ == '__main__':
    unittest.main()
