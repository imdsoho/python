# [generator]
# generator는 iterator 를 생성해 주는 function이다.
# iterator 는 next() 메소드를 이용해 데이터에 순차적으로 접근이 가능한 object 이다.
# generator는 일반함수와 다르지 않지만 yield가 있다.

# [Yield]
# generator 함수가 실행 중 yield를 만날 경우, 해당 함수는 그 상태로 정지(frozen)되며, 반환 값을 next()를 호출한 쪽으로 전달한다.
# 이후 함수는 일반적인 경우 처럼 종료되는 것이 아니라 그 상태로 유지된다.
# "frozen"은 로컬 변수, 명령 포인터, 스택 정보를 포함하여 모든 로컬 상태가 유지된다.

# [generator expression]
# An expression that returns an iterator.
# It looks like a normal expression followed by a for expression defining a loop variable, range,
# and an optional if expression.

# list comprehension 과 비슷하지만, [ ] 대신 ( ) 를 사용하면 된다.

# xrange() - python2

# python3 - custom function
def xrange(x):
    return iter(range(x))

[ i for i in xrange(10) if i % 2 ]
# [1, 3, 5, 7, 9]

( i for i in xrange(10) if i % 2 )
# <generator object <genexpr> at 0x1234567890>

# generator의 경우 데이터 값을 한꺼번에 메모리에 적재 하는 것이 아니라 next() 메소드를 통해 차례로 값에 접근할 때마다 메모리에 적재하는 방식이다.

# [참고] https://bluese05.tistory.com/56
# [참고] https://kkamikoon.tistory.com/90
