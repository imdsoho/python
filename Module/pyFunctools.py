# lru_cache()
# 메모이제이션을 구현한다.
# 메모이제이션은 이전에 실행한 값비싼 함수의 결과를 저장함을써 이전에 사용된 인수에 대해서
# 다시 계산할 필요가 없게 해준다.

import functools
from decorator_closure.decorator import clock2

@functools.lru_cache()
@functools.lru_cache(maxsize=128, typed=False)

@clock2
def fibonacci(n):
    if n < 2:
        return n

    return fibonacci(n-2) + fibonacci(n-1)

import html
def htmlize(obj):
    content = html.escape(repr(obj))
    print(repr(obj))
    return '<pre>{}</pre>'.format(content)


if __name__=='__main__':
    print(fibonacci(6))

    print(htmlize(abs))


