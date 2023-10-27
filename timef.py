'''Make a timing function to use on day8+ which we will call timef so that
it will not interfere with the standard library's timeit'''
import functools
import time

def timef(func):
    @functools.wraps(func)
    def wrapper_timef(*args, **kwargs):
        t0 = time.perf_counter()
        val = func(*args, **kwargs)
        t1 = time.perf_counter()
        print(f"Function {func.__name__!r} took {t1-t0:.5f} seconds")
        return(val)
    return(wrapper_timef)
