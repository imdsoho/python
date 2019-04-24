# 클로저는 함수 본체에서 정의하지 않고 참조하는 비전역 변수를 포함한 확장 범위를 가진 함수다.
# 함수 본체 외부에 정의된 비전역 변수에 접근할 수 있다는 것이 중요하다.

class Averager():
    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()
avg(10)
avg(11)

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

avg2 = make_averager()
avg2(10)
avg2(11)

# average 안에 있는 series는 자유 변수이다. 자유 변수라는 말은 지역 범위에 바인딩되어 있지 않은 변수를 의미한다.

# 파이썬이 컴파일된 함수 본체를 나타내는 __code__ 속성의 값
print (avg2.__code__.co_varnames)
# ('new_value', 'total')
print (avg2.__code__.co_freevars)
# ('series',)
print (avg2.__closure__)
# (<cell at 0x108852e58: list object at 0x1088ef888>,)
print (avg2.__closure__[0].cell_contents)
# [10, 11]

# 클로져는 함수를 정의할 때 존재하던 자유 변수에 대한 바인딩을 유지하는 함수다.
# 함수를 정의하는 범위가 사라진 후에 함수를 호출해도 자유 변수에 접근할 수 있다.


def make_averager_2():
    count = 0
    total = 0

    def averager(new_value):
        # count = count + 1             [ERROR] 지역변수 count 없음
        # total = total + new_value     [ERROR] 지역변수 total 없음

        # 변수를 nonlocal로 선언하면 함수 안에서 변수에 새로운 값을 할당하더라도 그 변수는 자유 변수이다.
        nonlocal  count, total
        count = count + 1
        total = total + new_value
        return total / count

    return averager

# 숫자, 문자열, 튜플 등 불변형은 읽을 수만 있고 값은 갱신할 수 없다.



