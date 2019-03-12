# lambda 인자 : 표현식
# 익명함수 다음 줄로 넘어가면 힙(heap) 메모리 영역에서 삭제

(lambda x, y: x + y)(10, 20)
# 30

# map() map(함수, 리스트) - 함수와 리스트를 인자로 받는다. 리스트에서 인자를 하나씩 함수에 적용시킨 다음 내용을 리스트에 저장
list(map(lambda x: x ** 2, range(5)))
# [0, 1, 4, 9, 16]

#게으른 연산
# 필요할 때 가져다 쓴다.
# iterator 객체
# next() 메소드로 데이터를 순차적으로 호출 가능한 object
# iterable한 객체를 iterator로 변환하고 싶다면, iter()라는 built-in function 사용
# for 문으로 looping 하는 동안, python 내부에서는 임시로 list를 iterator로 자동 변환
# 마지막 데이터까지 불러 오면 다음은 StopIteration exception 발생

# reduce() reduce(함수, 순서형 자료) - 순서형 자료(문자열, 리스트, 튜플)의 원소들을 누적하여 함수에 적용

from functools import reduce # python 3은 내장함수가 아니다.
reduce(lambda x, y: x + y, [0, 1,2,3,4])
# 10

reduce(lambda x, y: y + x, 'abcde')
# edcba

def sum(x, y):
    z = y + x

    return z

# [a,b,c,d,e]
# (a, b) -> ba # y + x
# (ba, c) -> cba # y + x

# filter() filter(함수, 리스트) - 리스트에 들어있는 원소들을 함수에 적용시켜 참인 값들을 리스트로 생성

list(filger(lambda x: x < 5, range(10)))
# [0, 1, 2, 3, 4]

# [참조] https://wikidocs.net/64
# [참조] https://wayhome25.github.io/cs/2017/04/03/cs-03/
