import unittest
from descriptors import Transport


class TestDescriptors(unittest.TestCase):
    def setUp(self):
        self.transport = Transport("Car", 1500, "red", 200)

    def test_create_valid_transport(self):
        try:
            self.transport
        except Exception as e:
            self.fail(f"Failed to create a valid Transport object: {e}")

    def test_invalid_attribute_types(self):

        with self.assertRaises(TypeError):
            self.transport.name = 123

        with self.assertRaises(TypeError):
            self.transport.weight = "heavy"

        with self.assertRaises(TypeError):
            self.transport.color = 255

        with self.assertRaises(TypeError):
            self.transport.speed = "fast"

    def test_negative_weight(self):
        with self.assertRaises(ValueError):
            self.transport.weight = -500

    def test_read_write_attributes(self):
        self.assertEqual(self.transport.name, "Car", "Failed to read 'name'")
        self.assertEqual(self.transport.weight, 1500, "Failed to read 'weight'")
        self.assertEqual(self.transport.color, "red", "Failed to read 'color'")
        self.assertEqual(self.transport.speed, 200, "Failed to read 'speed'")

        self.transport.name = "Bike"
        self.transport.weight = 200
        self.transport.color = "blue"
        self.transport.speed = 70
        self.assertEqual(self.transport.name, "Bike", "Failed to write 'name'")
        self.assertEqual(self.transport.weight, 200, "Failed to write 'weight'")
        self.assertEqual(self.transport.color, "blue", "Failed to write 'color'")
        self.assertEqual(self.transport.speed, 70, "Failed to write 'speed'")


if __name__ == '__main__':
    unittest.main()
