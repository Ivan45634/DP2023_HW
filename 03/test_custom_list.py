"""Implementation of CustomList"""
import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """Test cases for CustomList operations"""

    def setUp(self):
        """Initialization method"""
        self.lst1 = CustomList([1, 2, 3, 4])
        self.lst2 = CustomList([5, 4, 3, 2, 1])
        self.lst3 = CustomList([3, 0, 2])
        self.lst4 = CustomList()
        self.lst5 = [1, 2, 3, 4, 5]
        self.lst6 = [1, 2, 3]
        self.lst7 = [1, 2, 3, 4, 5, 6]
        self.lst8 = CustomList([1, 0, 1, 0])
        self.lst9 = CustomList([0, 1, 0, 1, 0])

    def test_addition(self):
        """
        test cases for addition
        """
        # Same size CustomLists
        temp_lst1 = self.lst1.copy()
        temp_lst2 = self.lst2.copy()
        temp_lst8 = self.lst8.copy()
        temp_lst9 = self.lst9.copy()

        self.assertEqual(list(self.lst1 + self.lst8),
                         list(CustomList([2, 2, 4, 4])))
        self.assertEqual(list(self.lst2 + self.lst9),
                         list(CustomList([5, 5, 3, 3, 1])))

        self.assertEqual(list(self.lst1), list(temp_lst1))
        self.assertEqual(list(self.lst2), list(temp_lst2))
        self.assertEqual(list(self.lst8), list(temp_lst8))
        self.assertEqual(list(self.lst9), list(temp_lst9))

        # Custom list(len=4) + List(len=5)
        temp_lst1 = self.lst1.copy()
        temp_lst5 = self.lst5.copy()

        self.assertEqual(list(self.lst1 + self.lst5),
                         list(CustomList([2, 4, 6, 8, 5])))
        self.assertEqual(list(self.lst5 + self.lst1),
                         list(CustomList([2, 4, 6, 8, 5])))

        self.assertEqual(self.lst5, temp_lst5)
        self.assertEqual(list(self.lst1), list(temp_lst1))

        # Custom list + Empty List
        temp_lst1 = self.lst1.copy()
        temp_lst4 = self.lst4.copy()

        self.assertEqual(list(self.lst1 + self.lst4), list(self.lst1))
        self.assertEqual(list(self.lst4 + self.lst1), list(self.lst1))

        self.assertEqual(list(self.lst1), list(temp_lst1))
        self.assertEqual(list(self.lst4), list(temp_lst4))

        # Custom list(len=5) + Smaller Custom list(len=3)
        temp_lst2 = self.lst2.copy()
        temp_lst3 = self.lst3.copy()

        self.assertEqual(list(self.lst2 + self.lst3),
                         list(CustomList([8, 4, 5, 2, 1])))
        self.assertEqual(list(self.lst3 + self.lst2),
                         list(CustomList([8, 4, 5, 2, 1])))

        self.assertEqual(list(self.lst2), list(temp_lst2))
        self.assertEqual(list(self.lst3), list(temp_lst3))

        # Custom list(len=4) + Bigger Custom list(len=5)
        temp_lst8 = self.lst8.copy()
        temp_lst9 = self.lst9.copy()

        self.assertEqual(list(self.lst8 + self.lst9),
                         list(CustomList([1, 1, 1, 1, 0])))
        self.assertEqual(list(self.lst9 + self.lst8),
                         list(CustomList([1, 1, 1, 1, 0])))

        self.assertEqual(list(self.lst8), list(temp_lst8))
        self.assertEqual(list(self.lst9), list(temp_lst9))

        # List + Custom list (same length)
        temp_lst6 = self.lst6.copy()
        temp_lst3 = self.lst3.copy()

        self.assertEqual(list(self.lst6 + self.lst3),
                         list(CustomList([4, 2, 5])))
        self.assertEqual(list(self.lst3 + self.lst6),
                         list(CustomList([4, 2, 5])))

        self.assertEqual(self.lst6, temp_lst6)
        self.assertEqual(list(self.lst3), list(temp_lst3))

        # Larger Custom List (len=5) and Smaller List (len=3)
        temp_lst2 = self.lst2.copy()
        temp_lst6 = self.lst6.copy()

        self.assertEqual(list(self.lst2 + self.lst6),
                         list(CustomList([6, 6, 6, 2, 1])))
        self.assertEqual(list(self.lst6 + self.lst2),
                         list(CustomList([6, 6, 6, 2, 1])))

        self.assertEqual(list(self.lst2), list(temp_lst2))
        self.assertEqual(self.lst6, temp_lst6)

    def test_subtraction(self):
        """
        test cases for subtraction
        """
        # Same size CustomLists
        temp_lst1 = self.lst1.copy()
        temp_lst8 = self.lst2.copy()

        self.assertEqual(list(self.lst1 - self.lst8),
                         list(CustomList([0, 2, 2, 4])))
        self.assertEqual(list(self.lst8 - self.lst1),
                         list(CustomList([0, -2, -2, -4])))

        self.assertEqual(list(self.lst1), list(temp_lst1))
        self.assertEqual(list(self.lst8), list(temp_lst8))

        # Custom list(len=4) - List(len=5)
        temp_lst1 = self.lst1.copy()
        temp_lst5 = self.lst5.copy()

        self.assertEqual(list(self.lst1 - self.lst5),
                         list(CustomList([0, 0, 0, 0, -5])))

        self.assertEqual(list(self.lst1), list(temp_lst1))
        self.assertEqual(self.lst5, temp_lst5)

        # Custom list - Empty List
        temp_lst1 = self.lst1.copy()
        temp_lst4 = self.lst4.copy()

        self.assertEqual(list(self.lst1 - self.lst4),
                         list(self.lst1))
        self.assertEqual(list(self.lst4 - self.lst1),
                         list(CustomList([-1, -2, -3, -4])))

        self.assertEqual(list(self.lst1), list(temp_lst1))
        self.assertEqual(list(self.lst4), list(temp_lst4))

        # Custom list(len=3) - Smaller Custom list(len=3)
        temp_lst2 = self.lst2.copy()
        temp_lst3 = self.lst3.copy()

        self.assertEqual(list(self.lst2 - self.lst3),
                         list(CustomList([2, 4, 1, 2, 1])))
        self.assertEqual(list(self.lst3 - self.lst2),
                         list(CustomList([-2, -4, -1, -2, -1])))

        self.assertEqual(list(self.lst2), list(temp_lst2))
        self.assertEqual(list(self.lst3), list(temp_lst3))

        # Custom list (len=4) - Bigger Custom list (len=3)
        temp_lst3 = self.lst3.copy()
        temp_lst9 = self.lst9.copy()

        self.assertEqual(list(self.lst3 - self.lst9),
                         list(CustomList([3, -1, 2, -1, 0])))
        self.assertEqual(list(self.lst9 - self.lst3),
                         list(CustomList([-3, 1, -2, 1, 0])))

        self.assertEqual(list(self.lst3), list(temp_lst3))
        self.assertEqual(list(self.lst9), list(temp_lst9))

        # List (len=3) - Custom list (len=4)
        temp_lst6 = self.lst6.copy()
        temp_lst8 = self.lst8.copy()

        self.assertEqual(list(self.lst6 - self.lst8),
                         list(CustomList([0, 2, 2, 0])))
        self.assertEqual(list(self.lst8 - self.lst6),
                         list(CustomList([0, -2, -2, 0])))

        self.assertEqual(self.lst6, temp_lst6)
        self.assertEqual(list(self.lst8), list(temp_lst8))

        # Larger Custom List (len=5) and Smaller List (len=3)
        temp_lst2 = self.lst2.copy()
        temp_lst6 = self.lst6.copy()

        self.assertEqual(list(self.lst2 - self.lst6),
                         list(CustomList([4, 2, 0, -1, -1])))
        self.assertEqual(list(self.lst6 - self.lst2),
                         list(CustomList([-4, -2, 0, 1, 1])))

        self.assertEqual(list(self.lst2), list(temp_lst2))
        self.assertEqual(self.lst6, temp_lst6)

    def test_comparison(self):
        """
        test cases for comparison operations
        """
        list1 = CustomList([1, 2, 3])
        list2 = CustomList([4, 5, 6])
        list3 = CustomList([6])
        list4 = CustomList()

        self.assertEqual(list1, list3)
        self.assertNotEqual(list3, list4)
        self.assertNotEqual(list1, list2)
        self.assertNotEqual(list2, list3)
        self.assertGreater(list1, list4)
        self.assertGreaterEqual(list1, list3)
        self.assertGreaterEqual(list2, list3)
        self.assertLess(list1, list2)
        self.assertLessEqual(list1, list3)
        self.assertLessEqual(list1, list2)

    def test_str(self):
        """
        test cases for __str__ override
        """
        custom_list = CustomList([1, 2, 3])
        self.assertEqual(str(custom_list), "[1, 2, 3], sum=6")
        custom_list.append("Hello, World!")
        self.assertEqual(str(custom_list), "[1, 2, 3], sum=6")


if __name__ == '__main__':
    unittest.main()
