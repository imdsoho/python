#@classmethod
#인스턴스가 아니라 클래스 자체에 작용하는 메소드
#@classmethod 데커레이터는 객체가 아닌 클래스에 연산을 수행하는 메소드를 정의한다.
#@classmethod는 메소드가 호출하는 방식을 변경해서 클래스 자체를 첫 번째 인수로 받게 만든다.

#@staticmethod
#@staticmethod 데커레이터는 메소드가 특별한 첫 번째 인수를 받지 않도록 메소드를 변경한다.
#@staticmethod 메소드는 모듈 대신 클래스 본체 안에 정의된 평범한 함수다.

class Demo:
    num = 0
    @classmethod
    def klassmeth(*args):
        #print(self.num)        # ERROR
        return args

    @classmethod
    def klassmeth2(cls, *args):
        print("[M]", cls.num)
        return args

    # 평범한 함수처럼 동작한다.
    # 함수가 클래스를 건드리지는 않지만, 해당 클래스와 관련이 있는 함수
    @staticmethod
    def statmeth(*args):
        #count = self.num + 1    # ERROR - static method이기 때문에 self로 접근할 수 없음
        return args

#print(Demo.klassmeth())
# (<class '__main__.Demo'>,)

#print(Demo.klassmeth('spam'))
# (<class '__main__.Demo'>, 'spam')

#print(Demo.klassmeth2())
# ()

#print(Demo.klassmeth2('spam'))
# ('spam',)

#print(Demo.statmeth())
# ()

print(Demo.statmeth('spam'))
# ('spam',)

demo1 = Demo.klassmeth('klass1','klass-2','klass-3')
print(demo1)
print(type(demo1))
#print(dir(demo1))

demo_inst = Demo()
demo_inst.klassmeth('instance')
demo_inst.num = 1
print("[1]", demo_inst.num)

demo_inst2 = Demo()
print("[2]", demo_inst2.num)

demo2 = Demo.klassmeth2('hello','world')
print(demo2)

import time
class MyTime():
    def __init__(self, hour, minutes, sec):
        self.hour = hour
        self.minutes = minutes
        self.sec = sec

    @staticmethod
    def now():
        t = time.localtime()
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

    @staticmethod
    def two_hours_later():
        t = time.localtime(time.time() + 7200)
        return MyTime(t.tm_hour, t.tm_min, t.tm_sec)

a = MyTime(15,20,58)
b = MyTime.now()
c = MyTime.two_hours_later()

class CoeffVar():
    coefficient = 1

    @classmethod
    def mul(cls, fact):
        return cls.coefficient * fact

class MulFive(CoeffVar):
    coefficient = 5

x = MulFive.mul(4)  # CoeffVar.mul(MulFive, 4)
print(x)

class Date :
    word = 'date : '

    def __init__(self, date):
        print('[constructor]', date, type(self), self.word)
        self.date = self.word + date

    @classmethod
    def now(cls):
        return cls("today")

    def show(self):
        print(self.date)

class KoreanDate(Date):
    word = '날짜 : '

a = KoreanDate.now() # Date.now(KoreaDate)
a.show()
# >>> [constructor] today <class '__main__.KoreanDate'> 날짜 :
# >>> classmethod 호출 -> KoreaDate 클래스에서 생성자 호출

#b = Date.now()
#b.show()
# >>> [constructor] today <class '__main__.Date'> date :
# >>> date : today

