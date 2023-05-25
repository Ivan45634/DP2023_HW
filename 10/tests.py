import unittest
import json
import ujson
import cjson

class TestCJson(unittest.TestCase):
    def setUp(self):
        self.json_str = '{"hello": 10, "world": "value"}'
        self.json_obj = {"hello": 10, "world": "value"}

    def test_loads(self):
        json_doc = json.loads(self.json_str)
        ujson_doc = ujson.loads(self.json_str)
        cjson_doc = cjson.loads(self.json_str)
        self.assertEqual(json_doc, ujson_doc)
        self.assertEqual(json_doc, cjson_doc)

    def test_dumps(self):
        json_str = json.dumps(self.json_obj)
        ujson_str = ujson.dumps(self.json_obj)
        cjson_str = cjson.dumps(self.json_obj)
        self.assertEqual(json_str, ujson_str)
        self.assertEqual(json_str, cjson_str)

if __name__ == '__main__':
    unittest.main()
