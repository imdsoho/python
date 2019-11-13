
class Base(object):
    def __init__(self):
        print('<Base>')
        #super(Base, self).__init__()
        super().__init__()
        print('</Base>')

class A(Base):
    def __init__(self):
        print('<A>')
        #super(A, self).__init__()              # python 2.7
        super().__init__()                      # (1)
        print('</A>')

class AA(Base):
    def __init__(self):
        print('<AA>')
        #super(AA, self).__init__()             # python 2.7
        super().__init__()                      # (2)
        print('</AA>')

class B(A, AA):
    def __init__(self):
        print('<B>')
        #super(B, self).__init__()
        super().__init__()
        print('</B>')

obj = B()
print(B.mro())


# URL: https://codeday.me/ko/qa/20190503/451426.html
'''
상속 체인에서 다음 “up”에 대한 함수 호출로 super를 보지 말아야합니다. 
대신, 적절하게 사용되면 super는 MRO의 모든 기능이이 순서로 호출되도록합니다. 
그러나 이러한 일이 발생하려면 super call()이 해당 체인의 모든 세그먼트에 있어야합니다.

따라서 A 또는 AA 중 하나에서 super call()을 제거하면 체인이 중단됩니다. 
제거하는 항목에 따라 체인이 A 또는 AA에서 중단됩니다.

> 중단 없음 (전체 MRO) : B, A, AA,베이스
> 사례 1 (A에서  super call() 없는 경우) : B, A
> 사례 2 (AA에서 super call() 없는 경우) : B, A, AA

따라서 제대로 작동하려면 모든 관련 유형에서 항상 super를 일관되게 사용하는 것이 중요합니다.

super()에 대해 더 자세히 알고 싶다면 올해 PyCon에서 Raymond Hettinger’s talk “Super considered super!”을 확인해야합니다. 
그것은 매우 잘 설명되어 있으며 또한 이해하기 쉬운 몇 가지 예 (실제 사람들을 포함합니다!)가 있습니다.
'''