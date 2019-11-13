# URL: https://bluese05.tistory.com/61

'''
python ABC(Abstract Base Class) 추상화 클래스

 python 의 ABC 클래스는 Base 클래스를 상속받는 파생 클래스가 반드시 Base 클래스의 메서드를 명시적으로 선언해서 구현하도록 강제하는 추상화 클래스 기능이다.

 그렇다면 이러한 기능이 왜 필요한가?

 이 기능의 필요성을 이해하려면 먼저 상속과 다형성에 대한 이해가 필요하다.

 OOP 의 가장 강력한 기능 중 하나인 상속(Inheritance)은 클래스의 재사용성을 높임으로서, 코드의 반복에 따른 유지 보수 비용을 낮추는데 큰 역할을 하였다. 이러한 상속의 개념과 함께 OOP 의 가장 중요한 특징 중 하나가 바로 다형성(Polymorphism) 이다. 
 여기서는 다형성에 대해서 좀 더 자세히 알아보자. 

 다형성(Polymorphism)

 In programming languages and type theory, polymorphism (from Greek πολύς, polys, "many, much" and μορφή, morphē, "form, shape") is the provision of a single interface to entities of different types. A polymorphic type is one whose operations can also be applied to values of some other type, or types.[2] There are several fundamentally different kinds of polymorphism:

- Wikipedia "Polymorphism (computer science)"

 다형성이란, 하나의 인터페이스를 통해 서로 다른 여러 타입을 제공하는 것을 의미한다. 보통 OOP 에서 말하는 다형성은 클래스에 선언된 메서드가 상속 받은 클래스에서 같은 이름으로 오버라이딩 되어 여러 형태로 동작함을 의미한다.

 설명하기 어려우니 예제로 살펴보자. 
 아래와 같은 BaseClass가 있다고 가정해보자. 여기에는 func1 과 func2 라는 메서드를 선언하였다.

>>> class BaseClass:
>>>    def func1(self):
>>>        pass

>>>    def func2(self):
>>>         pass

 그리고 이러한 BaseClass를 상속받는 클래스인 DerivedClass1 이 있다고 가정해보자. 이 클래스는 BaseClass 의 func1 과 func2 메소드를 각각 오버라이딩 해서 구현 하였다.

>>> class DerivedClass1(BaseClass):
>>>    def func1(self):
>>>        print "FUNC 1 in Derived1"

>>>    def func2(self):
>>>        print "FUNC 2 in Dervied1"

 또한 위 클래스와 동일하게 BaseClass를 상속 받는 또다른 클래스인 DerivedClas2 를 선언하였다. 마찬가지로 func1과 func2 를 오버라이딩 하였지만 그 내용은 약간 다르게 구현하였다. 

>>>class DerivedClass2(BaseClass):
>>>    def func1(self):
>>>         print "=================="
>>>         print "FUNC 1 in Derived2"
>>>         print "=================="

>>>    def func2(self):
>>>         print "=================="
>>>         print "FUNC 2 in Derived2"
>>>         print "=================="

만약, DerivedClass1 과 DerivedClass2 를 상황에 따라서 다르게 사용해야 한다면 어떨까. 
가장 간단한 방법은, 아래와 같이 클래스명을 변수로 받아 동적으로 import 한 후 func1 과 func2 를 호출하면 될 것이다.

>>> cls_name = "DerivedClass1"     # or "DerviedClass2"

>>> _m = getattr(__import__(cls_name, fromlist=[]), cls_name)()

>>> _m.func1()
>>> _m.func2()

 이렇게 된다면 DerivedClass1 과 DerivedClass2를 경우에 따라 변수를 이용하여 동적으로 사용 가능하게 된다. 즉, 클래스의 내용에 상관없이 호출하는 인터페이스만 맞춰주면 경우에 따라 다르게 동작되는 추상화된 형태로 사용이 가능하다는 의미이다.

 하지만, 이런 다형성을 이용한 추상화를 구현하는 경우 반드시 주의해야 할 부분이 있다. 바로 코드 유지보수에 대한 부분인데, 형태가 간단한 클래스는 문제가 되지 않지만, 클래스에 선언된 메서드가 많으면 이를 일일히 관리하기가 쉽지 않은게 현실이다.

만약 아래와 같이 BaseClass를 상속받는 클래스에 실수로 func2를 구현 안했다면 어떻게 될까.

>>> class DerivedClass3(BaseClass):
>>>    def func1(self):
>>>        print "FUNC1 in Derived3"

>>>    """
>>>    func2 method is not implemented yet..
>>>    """

 물론 엄마 클래스인 BaseClass의 func2 메서드를 실행하게 될 것이며 엄마클래스의 func2 메서드에서는 이를 pass 만 해놓도록 구현한 상태이기 때문에 아무것도 하지 않고 넘어갈 것이다. 이렇게 되면 나중에 이 부분의 구현을 추가 해야 된다는 사실을 잊고 넘어갈 수 있고, 추후 이로 인한 side effect 가 생길 여지가 있다. 

 그럼 이런 불상사를 피하기 위해 아래와 같이 BaseClass에 에러 호출부분을 추가해 보자.

>>> class BaseClass:
>>>    def func1(self):
>>>        raise NotImplementedError()

>>>    def func2(self):
>>>        raise NotImplementedError()
 
이렇게 해놓으면 BaseClass를 상속받을 파생 클래스에서 해당 메서드의 구현을 하지 않는다면, 자동으로 BaseClass의 메서드를 호출할 것이고,  NotImplentedError 를 발생시킬 것이다.

>>> FUNC1 in Dervied3
>>> Traceback (most recent call last):
>>>   File "D.py", line 5, in <module>
>>>    _m.func2()
>>>  File "/home/ubuntu/BaseClass.py", line 6, in func2
>>>    raise NotImplementedError()
>>> NotImplementedError

즉, 조금 더 엄격하게 상속 클래스들을 관리할 수 있게 되며, 추후 유지보수를 용이하게 할 수 있다. 
하지만, 이것보다 더 Strict 한 방식을 제공하는 것이 오늘 알아볼 ABC 클래스이다.



ABC (Abstract Base Class)

아래는 BaseClass에 abc를 적용한 예이다.

import abc 

>>> class BaseClass:

>>>    __metaclass__ = abc.ABCMeta

>>>    @abc.abstractmethod
>>>    def func1(self):
>>>        pass

>>>    @abc.abstractmethod
>>>    def func2(self):
>>>        pass


추상화 시키고자 하는 메서드에 데코레이터로 @abstractmethod 를 선언해 주면 된다.
이렇게 적용하게 되면, BaseClass를 상속받는 모든 파생 클래스에서 해당 메서드를 선언해서 구현하지 않으면, 에러를 발생시키게 된다.

>>> Traceback (most recent call last):
>>>  File "D.py", line 2, in <module>
>>>    _m = getattr(__import__(cls_name, fromlist=[]), cls_name)()
>>> TypeError: Can't instantiate abstract class DerivedClass3 with abstract methods func2

그렇다면, ABC를 사용하는 것과 NotImplementedError 를 메서드마다 선언해 놓는 것은 어떤 차이가 있을까.

첫째로, abc 클래스를 이용하게 되면, 해당 BaseClass 는 인스턴스화 될 수 없다. 단지 파생 클래스 구현을 위한 추상화 기능 제공 역할을 하게 될 뿐이다.

>>> from BaseClass import BaseClass
>>> 
>>> base = BaseClass()

>>> Traceback (most recent call last):
>>>  File "<stdin>", line 1, in <module>
>>> TypeError: Can't instantiate abstract class BaseClass with abstract methods func1, func2

 두번째, abc 클래스를 이용하게 될 경우 에러 발생 시점이 다르다.
 메서드에 raise를 이용해 NotImplementedError 를 선언해 놓은 경우에는 런타임 상황에서 해당 메서드가 실제로 호출이 되는 시점에 에러를 발생시키게 되지만, abc 를 이용하는 경우에는 해당 모듈이 import 되는 순간부터 에러를 발생시키게 된다. 즉, abc 클래스를 이용하는 경우 조금 더 strict 한 모듈 관리가 가능해 진다는 점이다.

>>> Traceback (most recent call last):
>>>  File "D.py", line 2, in <module>
>>>    _m = getattr(__import__(cls_name, fromlist=[]), cls_name)()
>>> TypeError: Can't instantiate abstract class DerivedClass3 with abstract methods func2

위에서 보는것 같이 에러 발생 시점이 해당 모듈을 import하는 순간 발생 된다.


[참고]
•	https://docs.python.org/2/library/abc.html
•	https://dbader.org/blog/abstract-base-classes-in-python
•	https://en.wikipedia.org/wiki/Polymorphism_(computer_science)
'''