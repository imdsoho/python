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

print (avg2.__code__.co_varnames)
print (avg2.__code__.co_freevars)
