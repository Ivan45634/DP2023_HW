import functools
import cProfile


def profile_deco(func):
    profiler = cProfile.Profile()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        profiler.enable()
        result = func(*args, **kwargs)
        profiler.disable()
        wrapper.print_stat = lambda: profiler.print_stats()
        return result

    return wrapper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


add(1, 2)
add(4, 5)
sub(4, 5)

add.print_stat()
sub.print_stat()
