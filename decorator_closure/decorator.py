import time

def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

# def factorial(n):
# return 1 if n < 2 else n*factorial(n-1)
# factorial = clock(factorial)


import time
import functools

def clock2(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()

        result = func(*args, **kwargs)

        elapsed = time.time() - t0
        name = func.__name__

        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', '.join(pairs))

        arg_str = ', '.join(arg_list)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

        return result
    return clocked

# clock2()가 clocked()를 반환하고, 데커레이트될 함수에 clocked()가 적용된다.

@clock2
def factorial2(n):
    return 1 if n < 2 else n*factorial(n-1)


# 누적된 데커레이터
#def d1():
#    pass

#def d2():
#s    pass

#@d1
#@d2
#def f():
#    print('f')
# 와
#f = d1(d2(f))
# 는 동일하다.


# 매개변수화된 clock 데커레이터
import time
DEFAULT_FMT = '[{elapsed:0.8f}s {name}({args}) -> {result}'

def clock3(fmt=DEFAULT_FMT):
    def decorate(func):             # 실제 데커레이터
        def clocked(*_args):        # 데커레이트 된 함수를 래핑한다.
            t0 = time.time()
            _result = func(*_args)  # 데커레이트된 함수의 실제 결과를 _result에 저장한다.
            print('[*]', func.__name__)
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args)
            result = repr(_result)
            print(fmt.format(**locals()))   # **locals()를 사용하면 fmt가 clocked()의 지역 변수를 모두 참조할 수 있게 한다.
            return _result
        return clocked
    return decorate

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling snooze(6)')
    print('6! = ', factorial(6))
    # 파이썬 인터프리터가 내부적으로 clocked()를 factorial에 할당했다.
    # print(factorial.__name__) => >>> 'clocked'
    # factorial(n)을 호출하면 clocked(n)이 실행된다.
    # 데커레이트된 함수를 동일한 인수를 받는 함수로 교체하고, 데커레이트된 함수가 반환해야 하는 값을 반환하면서 추가적인 처리를 수행한다.

    print('6! = ', factorial2(6))

    @clock3()
    def snooze2(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze2(.123)


