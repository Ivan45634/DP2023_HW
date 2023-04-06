"""Implementation of CustomList"""
import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """Test cases for CustomList operations"""

    def setUp(self):
        """Initialization method"""
        self.custom_list_1 = CustomList([1, 2, 3])
        self.custom_list_2 = CustomList([4, 5, 6])
        self.custom_list_3 = CustomList([1, 2, 3])
        self.custom_list_4 = CustomList([1, 2, 3, 4])
        self.custom_list_5 = CustomList([1, 2])

    def test_add_equal_length_lists(self):
        """Test case for custom lists with equal length"""
        result = self.custom_list_1 + self.custom_list_2
        self.assertEqual(list(result), list(CustomList([5, 7, 9])))

    def test_add_first_list_shorter(self):
        """Test case for
        short length custom list and long length custom list"""
        result = self.custom_list_1 + self.custom_list_4
        self.assertEqual(list(result), list(CustomList([2, 4, 6, 4])))

    def test_add_second_list_shorter(self):
        """Test case for
        long length custom list and short length custom list"""
        result = self.custom_list_4 + self.custom_list_1
        self.assertEqual(list(result), list(CustomList([2, 4, 6, 4])))

    def test_subtract_equal_length_lists(self):
        """Test case for subtract operation for equal length custom list"""
        result = self.custom_list_2 - self.custom_list_1
        self.assertEqual(list(result), list(CustomList([3, 3, 3])))

    def test_subtract_first_list_longer(self):
        """Test case for subtract operation
        for long length custom list and short length custom list"""
        result = self.custom_list_4 - self.custom_list_1
        self.assertEqual(list(result), list(CustomList([0, 0, 0, 4])))

    def test_subtract_second_list_longer(self):
        """Test case for subtract operation
        for long length custom list and short length custom list"""
        result = self.custom_list_1 - self.custom_list_5
        self.assertEqual(list(result), list(CustomList([0, 0, 3])))

    def test_equal(self):
        """Test case for subtract operation
        for long length custom list and short length custom list"""
        self.assertTrue(self.custom_list_1 == self.custom_list_3)

    def test_not_equal(self):
        """Test case for not equal lists"""
        self.assertTrue(self.custom_list_1 != self.custom_list_2)

    def test_greater_than(self):
        """Test case for checking operation >"""
        self.assertTrue(self.custom_list_2 > self.custom_list_1)

    def test_greater_than_or_equal(self):
        """Test case for checking operation >="""
        self.assertTrue(self.custom_list_2 >= self.custom_list_1)
        self.assertTrue(self.custom_list_1 >= self.custom_list_3)

    def test_less_than(self):
        """Test case for checking operation <"""
        self.assertTrue(self.custom_list_1 < self.custom_list_2)

    def test_less_than_or_equal(self):
        """Test case for checking operation <="""
        self.assertTrue(self.custom_list_1 <= self.custom_list_3)
        self.assertTrue(self.custom_list_1 <= self.custom_list_2)


unittest.main()
