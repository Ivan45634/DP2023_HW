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
    json_doc = json.loads(json_str)

    if required_fields is None:
        print("No required fields. Let's check existing keys!")
        required_fields = list(json_doc.keys())

    if keywords is None:
        return None

    for field in required_fields:
        if field not in json_doc:
            continue

        value = json_doc[field]

        for keyword in keywords:
            # считаем, что значение поля - набор слов, разделенных пробелом
            if keyword in value.split():
                if keyword_callback is not None:
                    keyword_callback(field, keyword)
                    continue
                raise TypeError
