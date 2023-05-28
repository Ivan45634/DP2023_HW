class CustomMeta(type):
    """ Metaclass """
    def __new__(mcs, name, bases, attribute_dict):
        new_attribute_dict = {}
        for attribute_key, attribute_val in attribute_dict.items():
            if not attribute_key.startswith('__'):
                attribute_key = 'custom_' + attribute_key
            new_attribute_dict[attribute_key] = attribute_val

        def _setattr(self, attr_name, value):
            if not attr_name.startswith('__'):
                attr_name = 'custom_' + attr_name
            object.__setattr__(self, attr_name, value)

        cls = super().__new__(mcs, name, bases, new_attribute_dict)
        cls.__setattr__ = _setattr
        return cls


class CustomClass(metaclass=CustomMeta):
    """ CustomClass """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"
