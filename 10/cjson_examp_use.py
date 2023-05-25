import cjson

json_string = '{"k1": "abcde", "k2": 42}'
json_dict = cjson.loads(json_string)
print(json_dict)

json_str = cjson.dumps(json_dict)
print(json_str)
