#-*- coding: utf-8 -*-

from itertools import islice, dropwhile, permutations, combinations, combinations_with_replacement

def count(n):
    while True:
        yield n
        n += 1

c = count(5)

for x in itertools.islice(c, 10, 20):
    print(x)

# islice()
# 순환 객체의 앞 부분 자르기

# dropwhile()
# 순환 객체의 내용 중 일정한 조건에 맞는 내용을 생략하기

# permutations()
# 아이템 컬렉션을 받아 가능한 모든 순열을 튜플 시퀀스로 생성

# combinations()
# 입력 받은 아이템의 가능한 조합 생성

# combinations_with_replacement()
# 중복을 허용하여 가능한 조합 생성
