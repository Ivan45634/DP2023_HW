class CustomMeta(type):
    """ Metaclass """
    def __new__(mcs, name, bases, attr_dict):
        new_attr_dict = {}
        for name, val in attr_dict.items():
            new_attr_dict[f'custom_{name}'] = val
        return super().__new__(mcs, name, bases, new_attr_dict)

    def __init__(cls, name, bases, attr_dict):
        new_attr_dict = {}
        for name, val in attr_dict.items():
            new_attr_dict[f'custom_{name}'] = val
        return super().__new__(name, bases, new_attr_dict)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class CustomClass(metaclass=CustomMeta):
    """ CustomClass """
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class Integer:
    """A descriptor that accepts only integer values"""
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.__class__.__name__} only accepts integer values")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name


class String:
    """A descriptor that accepts only string values"""
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError(f"{self.__class__.__name__} only accepts string values")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name


class PositiveInteger:
    """A descriptor that accepts only positive integer values"""
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.__class__.__name__} only accepts integer values")
        if value < 0:
            raise ValueError(f"{self.__class__.__name__} only accepts positive values")
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set_name__(self, owner, name):
        self.name = name

class Transport:
    name = String()
    weight = PositiveInteger()
    color = String()
    speed = Integer()

    def __init__(self, name, weight, color, speed):
        self.name = name
        self.weight = weight
        self.color = color
        self.speed = speed

    def __str__(self):
        return f"{self.color} {self.name} weighs {self.weight}kg and can go up to {self.speed}km/h"

if __name__ == "__main__":
    car = Transport("BMW X5", 2000, "black", 250)
    print(car)
    bike = Transport("Suzuki GS500F", 200, "blue", 180)
    print(bike)
    #car.speed = "300"
    #bike.weight = -20
    a = CustomClass()
    print(a.custom_x)

