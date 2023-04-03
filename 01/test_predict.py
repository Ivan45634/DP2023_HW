import unittest
from unittest import mock

from some_model import predict_message_mood
from some_model import SomeModel


class TestSomeModel(unittest.TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_predict_message_mood_bad(self):
        with mock.patch.object(SomeModel, "predict", return_value=0.2):
            message = "bad message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "неуд")

    def test_predict_message_mood_good(self):
        with mock.patch.object(SomeModel, "predict", return_value=0.9):
            message = "good message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "отл")

    def test_predict_message_mood_normal(self):
        with mock.patch.object(SomeModel, "predict", return_value=0.5):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "норм")
        with mock.patch.object(SomeModel, "predict", return_value=0.3):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "норм")
        with mock.patch.object(SomeModel, "predict", return_value=0.8):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "норм")
