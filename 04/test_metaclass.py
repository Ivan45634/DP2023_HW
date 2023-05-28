import unittest
from metaclass import CustomClass


class TestCustomMeta(unittest.TestCase):
    def setUp(self):
        self.obj = CustomClass()

    def test_class_fields_renamed(self):
        self.assertEqual(self.obj.custom_x, 50)
        with self.assertRaises(AttributeError):
            self.obj.x

    def test_class_functions_renamed(self):
        self.assertEqual(self.obj.custom_line(), 100)
        with self.assertRaises(AttributeError):
            self.obj.line()

    def test_obj_fields_renamed(self):
        self.assertEqual(self.obj.custom_val, 99)
        with self.assertRaises(AttributeError):
            self.obj.val

    def test_class_attributes(self):
        assert CustomClass.custom_x == 50
        with self.assertRaises(AttributeError):
            CustomClass.x

    def test_dynamic_added_attributes(self):
        self.obj.dynamic = "added later"
        self.assertEqual(self.obj.custom_dynamic, "added later")
        with self.assertRaises(AttributeError):
            self.obj.dynamic
