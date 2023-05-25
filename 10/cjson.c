#include <Python.h>
#include <jansson.h> // для работы с JSON

static PyObject *
cjson_loads(PyObject *self, PyObject *args)
{
    const char *json_str;
    if (!PyArg_ParseTuple(args, "s", &json_str))
    {
        PyErr_Format(PyExc_TypeError, "Expected a string");
        return NULL;
    }

    json_error_t error;
    json_t *root = json_loads(json_str, 0, &error);

    if (!root)
    {
        PyErr_Format(PyExc_ValueError, "Invalid JSON: %s", error.text);
        return NULL;
    }

    if (!json_is_object(root))
    {
        json_decref(root);
        PyErr_Format(PyExc_TypeError, "Expected JSON object");
        return NULL;
    }

    PyObject *py_dict = PyDict_New();
    const char *key;
    json_t *value;
    json_object_foreach(root, key, value)
    {
        PyObject *py_key = Py_BuildValue("s", key);
        PyObject *py_value = NULL;

        if (json_is_string(value))
        {
            py_value = Py_BuildValue("s", json_string_value(value));
        }
        else if (json_is_integer(value))
        {
            py_value = Py_BuildValue("i", json_integer_value(value));
        }
        PyDict_SetItem(py_dict, py_key, py_value);
        Py_DECREF(py_key);
        Py_DECREF(py_value);
    }

    json_decref(root);
    return py_dict;
}

static PyObject *
cjson_dumps(PyObject *self, PyObject *args)
{
    PyObject *input_dict;
    if (!PyArg_ParseTuple(args, "O!", &PyDict_Type, &input_dict))
    {
        PyErr_Format(PyExc_TypeError, "Expected dict");
        return NULL;
    }

    json_t *root = json_object();
    PyObject *key, *value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(input_dict, &pos, &key, &value))
    {
        const char *key_str = PyUnicode_AsUTF8(key);

        if (PyUnicode_Check(value))
        {
            json_object_set_new(root, key_str, json_string(PyUnicode_AsUTF8(value)));
        }
        else if (PyLong_Check(value))
        {
            json_object_set_new(root, key_str, json_integer(PyLong_AsLong(value)));
        }
    }

    char *json_str = json_dumps(root, JSON_INDENT(2));
    PyObject *py_json_str = Py_BuildValue("s", json_str);

    free(json_str);
    json_decref(root);
    return py_json_str;
}

static PyMethodDef CJsonMethods[] = {
    {"loads", cjson_loads, METH_VARARGS, "Deserialize JSON string."},
    {"dumps", cjson_dumps, METH_VARARGS, "Serialize PyObject to JSON string."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef cjson = {
    PyModuleDef_HEAD_INIT,
    "cjson",
    NULL,
    -1,
    CJsonMethods
};

PyMODINIT_FUNC
PyInit_cjson(void)
{
    return PyModule_Create(&cjson);
}
