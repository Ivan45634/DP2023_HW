import time
import weakref


class Value:
    def __init__(self, value):
        self.value = value


class RegularClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class SlotsClass:
    __slots__ = ('a', 'b', 'c')

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


class WeakrefClass:
    def __init__(self, a, b, c):
        self.a = weakref.ref(a)
        self.b = weakref.ref(b)
        self.c = weakref.ref(c)


def create_objects(cls, num):
    values = [Value(i) for i in range(3*num)]
    objs = [cls(values[3*i], values[3*i + 1], values[3*i + 2]) for i in range(num)]
    start_time = time.time()
    for obj in objs:
        if isinstance(obj, WeakrefClass):
            obj.a().value = obj.a().value + 1
            obj.b().value = obj.b().value + 2
            obj.c().value = obj.c().value + 3
        else:
            obj.a.value = obj.a.value + 1
            obj.b.value = obj.b.value + 2
            obj.c.value = obj.c.value + 3
    print("Time for {} instances of {}: {}".format(num, cls.__name__, time.time() - start_time))


num_instances = 1000000
create_objects(RegularClass, num_instances)
create_objects(SlotsClass, num_instances)
create_objects(WeakrefClass, num_instances)
