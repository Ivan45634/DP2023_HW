import timeit
import json
import ujson
import cjson

# large_json = '{"key1": "value1", "key2": "value2"}'

def test_json_loads():
    json.loads(large_json)

def test_ujson_loads():
    ujson.loads(large_json)

def test_cjson_loads():
    cjson.loads(large_json)

def test_json_dumps():
    json.dumps(large_json)

def test_ujson_dumps():
    ujson.dumps(large_json)

def test_cjson_dumps():
    cjson.dumps(large_json)

if __name__ == '__main__':
    test_functions = [test_json_loads, test_ujson_loads, test_cjson_loads,
                      test_json_dumps, test_ujson_dumps, test_cjson_dumps]

    for test_function in test_functions:
        test_name = test_function.__name__
        duration = timeit.timeit(test_function, number=100)
        print(f"{test_name}: {duration:.6f}")
