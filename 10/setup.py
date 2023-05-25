from distutils.core import setup, Extension

cjson_module = Extension('cjson',
                           sources=['cjson.c'],
                           libraries=['jansson'])

setup(name='CJson',
      version='1.0',
      description='Python JSON library using C API',
      ext_modules=[cjson_module])
