"""Юнит-тесты для some_model.py"""
from unittest import mock
import unittest
from some_model import predict_message_mood
from some_model import SomeModel


class TestSomeModel(unittest.TestCase):
    """
    Класс с тестами
    """
    def setUp(self):
        self.model = SomeModel()

    def test_predict_message_mood_bad(self):
        """
        Проверка, что функция predict_message_mood возвращает "неуд"
         при передаче сообщения с негативной окраской.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.2):
            message = "bad message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "неуд")

    def test_predict_message_mood_good(self):
        """
        Проверка, что функция predict_message_mood возвращает "отл"
         при передаче сообщения с положительной окраской.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.9):
            message = "good message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "отл")

    def test_predict_message_mood_normal(self):
        """
        Проверка, что ф-ия predict_message_mood корректно возвращает значение
         при передаче сообщения со средней окраской.
        Также проверяется,
        что при граничных значениях окраски ф-ия возвращает верный результат.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.5):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "норм")
        with mock.patch.object(SomeModel, "predict", return_value=0.29):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "неуд")
        with mock.patch.object(SomeModel, "predict", return_value=0.9):
            message = "normal message"
            result = predict_message_mood(message, self.model)
            self.assertEqual(result, "отл")

    def test_predict_message_mood_called(self):
        """
        Проверка, что функция вызывается от переданного message
        """
        message = "Hello, how are you doing?"
        with mock.patch.object(SomeModel, "predict", return_value=0.999) as mock_call:
            predict_message_mood(message, self.model)
            mock_call.assert_called_with(message)

    def test_predict_with_invalid_input(self):
        """
        Проверка, что функция генерирует ошибку TypeError
         при неправильных входных данных.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.4):
            message = 123
            with self.assertRaises(TypeError):
                predict_message_mood(message, self.model)

    def test_predict_with_new_pos_threshold(self):
        """
        Проверка, что функция работает с измененным порогом good_thresholds.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.9):
            message = "test message"
            res = predict_message_mood(message, self.model, good_thresholds=0.95)
            self.assertEqual(res, "норм")

    def test_predict_with_new_neg_threshold(self):
        """
        Проверка, что функция работает с измененным порогом bad_thresholds.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.03):
            message = "test message"
            res = predict_message_mood(message, self.model, bad_thresholds=0.05)
            self.assertEqual(res, "неуд")

    def test_predict_with_new_pos_and_neg_thresholds(self):
        """
        Проверка, что функция работает с измененными порогами
         good_thresholds и bad_thresholds.
        """
        with mock.patch.object(SomeModel, "predict", return_value=0.8):
            message = "test message"
            res = predict_message_mood(message, self.model, good_thresholds=0.7, bad_thresholds=0.3)
            self.assertEqual(res, "отл")


if __name__ == '__main__':
    unittest.main()
