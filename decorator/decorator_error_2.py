from time import time, sleep
from functools import wraps

def traced_function_wrong(function):
    print("%s 함수 실행 ", function)
    start_time = time()

    @wraps(function)
    def wraped(*args, **kwargs):
        result = function(*args, **kwargs)
        print("%s 실행시간: %.2fs", function, time() - start_time)
        return result

    return wraped

def traced_function(function):
    @wraps(function)
    def wraped(*args, **kwargs):
        print("%s 함수 실행 ", function.__qualname__)
        start_time = time()

        result = function(*args, **kwargs)

        print("%s 실행시간: %.2fs", function, time() - start_time)
        return result

    return wraped

@traced_function_wrong
def process_with_delay(callback, delay=0):
    sleep(delay)

    return callback()

proc = process_with_delay(str)
