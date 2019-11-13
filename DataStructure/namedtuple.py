# collections.namedtuple()은 실제로 표준 파이썬 tuple 타입의 서브클래스를 반환하는 팩토리 메소드이다.
# 타입 이름과 포함해야 할 필드를 전달하면 인스턴스화 가능한 클래스를 반환

from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('abc@example.com', '2012-10-19')
#print (type(sub))

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total

# namedtuple은 수정할 수 없다.
# 속성을 수정하려면 namedtuple 인스턴스의 _replace() 메소드를 사용해야 한다.
# 값을 치환하여 새로운 namedtuple을 생성한다.

s = Stock('ACME', 100, 123.45)
s = s._replace(shares=75)

# 프로토타입 튜플 생성
Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototyp = Stock('', 0, 0.0, None, None)
def dict_to_stock(s):
    return stock_prototyp._replace(**s)


grades = []
Grade = namedtuple('Grade', ('score', 'weight'))
g1 = Grade(5, 1)
g2 = Grade(4.5, 1)
grades.append(g1)
grades.append(g2)

for g in grades:
    print(g.score)
