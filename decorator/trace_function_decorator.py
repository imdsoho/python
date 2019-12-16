from functools import wraps
from time import time

def trace_function(function):
    @wraps(function)
    def wrapped(*args, **kwargs):
        print("%s function exec ", function.__qualname__)
        start_time = time()

        result = function(*args, **kwargs)
        print("%s function end : %.2fs ", function.__qualname__, time() - start_time)

        return result

    return wrapped
