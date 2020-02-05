from typing import List
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# 형 검사 통과; float의 리스트는 Vector로 적합합니다.
new_vector = scale(2.0, [1.0, -4.2, 5.4])


from typing import NewType

UserId = NewType('UserId', int)

# 실행 시간에 실패하고 형 검사를 통과하지 못합니다
#class AdminUserId(UserId): pass # Sub Class를 생성하지 못함

# sub new type을 만들 수 있음
ProUserId = NewType('ProUserId', UserId)


