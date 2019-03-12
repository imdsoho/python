# iterable의 의미는 member를 하나씩 차례로 반환 가능한 object를 말한다. iterable 의 예로는 sequence type인 list, str, tuple 이 대표적이다.

# iterable 객체 - 반복 가능한 객체 대표적으로 iterable한 타입 - list, dict, set, str, bytes, tuple, range

for x in range(5):
    print x

# 위와 같은 for 문은 사실 range() 로 생성된 list가 iterable 하기 때문에 순차적으로 member들을 불러서 사용이 가능했던 것이다. non-sequence type 인 dict 나 file 도 iterable 하다고 할 수 있다. dict 또한 for 문을 이용해 순차적으로접근이 가능하다.
# 또한 iter() 나 getitem() 메소드로 정의된 class 는 모두 iterable 하다고 할 수 있다.
# iterable은 for loop 말고도, zip(), map()과 같이 sequence한 특징을 필요로 하는 작업에 유용하게 사용된다. zip() 이나 map() 함수의 경우 iterable 을 argument 로 받는 것으로 정의되어 있다.

b = {1, 2, 3}
dir(b)

# ['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']

b_iter = b.__iter__()
type(b_iter)
# <class 'set_iterator'>

#Iterator 는 next() 메소드로 데이터를 순차적으로 호출 가능한 object 이다. 만약 next() 로 다음 데이터를 불러 올수 없을 경우 (가장 마지막 데이터인 경우) StopIteration exception을 발생시킨다.

# iterator 객체 - 값을 차례대로 꺼낼 수 있는 객체입니다. iterator는 iterable한 객체를 내장함수 또는 iterable객체의 메소드로 객체를 생성할 수 있습니다. iterable객체는 매직메소드 iter 메소드를 가지고 있습니다
# iterable 한 object들은 iterator 인가? 결론부터 말하자면, iterable 이라고 해서 반드시 iterator 라는 것은 아니다.

x = [1,2,3]
next(x)
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: list object is not an iterator

# list 는 iterable 이지만, 위와 같이 next() 메소드로 호출해도 동작하지 않는다. iterator 가 아니라는 에러 메시지를 볼 수 있다. 만약, iterable 을 iterator 로 변환하고 싶다면, iter() 라는 built-in function 을 사용하면 된다.

x = [1,2,3]
type(x)
# <type 'list'>

y = iter(x)
type(y)
# <type 'listiterator'>

[참고] https://bluese05.tistory.com/55
[참고] https://wikidocs.net/16068
