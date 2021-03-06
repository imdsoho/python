b = 6

def f2(a):
    #print(a)

    #print(b)
    # *** ERROR 발생 ***
    # 파이썬이 함수 본체를 컴파일할 때 b가 함수 안에서 할당되므로 b를 지역 변수로 판단한다.
    # 버그가 아니라 설계 결정사항
    # 파이썬은 변수가 선언되어 있기를 요구하지 않지만, 함수 본체 안에서 할당된 변수는 지역 변수로 판단한다.

    b = 9
f2(3)

def f2_refactor(a):
    global b    # 지역변수 b를 전역 변수로 처리 - 에러 발생 없음
    #print(a)
    print("f2_refactor call() - used global varialbe " + str(b))
    b = 9
f2_refactor(3)


from dis import dis
#dis(f2_refactor)        # assembly

cheeseName = ['Red Leicester', 'Tilsit', 'Brie', 'Parmesan']
for cheese in cheeseName:
    print(cheese)

print(dir())
print("var in for loop - " + cheese)

cache = cheese
print("assign var : " + cache)


class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return 'Cheese(%r)' % self.kind

import weakref
stock = weakref.WeakValueDictionary()
catalog = [Cheese('Red Leicester'), Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))

for key in stock.keys():
    #print(type(stock.get(key)))
    #print(id(stock.get(key)))
    print(stock.get(key))

print(dir())

