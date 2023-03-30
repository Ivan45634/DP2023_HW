"""This module provides function for working with JSON data."""
import json


def parse_json(
    json_str: str,
    required_fields=None,
    keywords=None,
    keyword_callback=None
):
    """
    Parses the specified JSON string and runs keyword_callback function.
    """

    # Парсим json
    json_doc = json.loads(json_str)

    # Если required_fields не задан, считаем, что нужно обработать все поля
    if required_fields is None:
        required_fields = list(json_doc.keys())

    # Если keywords не задан, просто ничего не делаем
    if keywords is None:
        return

    # Проходимся по нужным полям
    for field in required_fields:
        # Если поле не найдено, то переходим к следующему
        if field not in json_doc:
            continue
        # Получаем значение поля
        value = json_doc[field]

        # Проходим по ключевым словам
        for keyword in keywords:
            # Если ключевое слово найдено в значении поля, вызываем обработчик
            if keyword in value:
                if keyword_callback is not None:
                    keyword_callback(keyword, field, value)
                # Если нужно обработать только первое найденное ключевое слово,
                # то выходим из цикла по ключевым словам
                break
