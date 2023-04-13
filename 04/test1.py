import unittest

from metaclass import Integer, String, PositiveInteger

class TestDescriptors(unittest.TestCase):

    def test_integer_acceptance(self):
        descriptor = Integer()
        with self.assertRaises(TypeError):
            descriptor.__set__(self, None, "string")
        descriptor.__set__(self, None, 123)
        self.assertEqual(descriptor.__get__(self, None), 123)

    def test_string_acceptance(self):
        descriptor = String()
        with self.assertRaises(TypeError):
            descriptor.__set__(self, None, 123)
        descriptor.__set__(self, None, "string")
        self.assertEqual(descriptor.__get__(self, None), "string")

    def test_positive_integer_acceptance(self):
        descriptor = PositiveInteger()
        with self.assertRaises(TypeError):
            descriptor.__set__(self, None, "string")
        with self.assertRaises(ValueError):
            descriptor.__set__(self, None, -123)
        descriptor.__set__(self, None, 123)
        self.assertEqual(descriptor.__get__(self, None), 123)


if __name__ == '__main__':
    unittest.main()
