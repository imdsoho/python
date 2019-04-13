b = 6
'''def f2(a):
    print(a)
    print(b)
    b = 9

f2(3)'''

# *** ERROR 발생 ***
# 파이썬이 함수 본체를 컴파일할 때 b가 함수 안에서 할당되므로 b를 지역 변수로 판단한다.
# 버그가 아니라 설계 결정사항
# 파이썬은 변수가 선언되어 있기를 요구하지 않지만, 함수 본체 안에서 할당된 변수는 지역 변수로 판단한다.

def f2_refactor(a):
    global b    # 지역변수 b를 전역 변수로 처리 - 에러 발생 없음
    print(a)
    print(b)
    b = 9

from dis import dis
dis(f2_refactor)

