mylist = [1,4,-5,7,10,-7,2,3,-1]

comp = [n for n in mylist if n > 0]

# 생성자 표현식 사용 - generator
# https://github.com/imdsoho/python/blob/master/Basic/generator_yield.py

comp2 = (n for n in mylist if n > 0)
print(type (comp2))
# <class 'generator'>

for x in comp2:
    print(x)

values = ['1','4','-5','7','10','-7','2','N/A']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print(ivals)

# filter()는 iterator를 생성한다.

# 데이터 변경
import math
data= [math.sqrt(n) for n in mylist if n > 0]

# 새로운 값으로 치환
clip_neg = [n if n > 0 else 0 for n in mylist]


from itertools import compress
# 순환 가능한 값과 Boolean 셀렉터를 입력으로 받음
# iterator 반환 -> list() 함수를 사용하여 리스트로 변환

address = ['A','B', 'C', 'D', 'E']
counts = [0,3,7,1,9]

more5 = [n > 5 for n in counts]
# [False, False, True, False, True]
# Boolean 시퀀스 생성

list(compress(address, more5))
# [C,E]
