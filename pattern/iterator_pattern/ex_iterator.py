s = 'ABC'       # 반복형
it = iter(s)    # 반복자
while True:
    try:
        print(next(it))
    except StopIteration:
        del it
        break

'''
반복자(iterator) 표준 인터페이스

__next__()
    다음에 사용할 항목을 반환한다. 더 이상 항목이 남아 있지 않으면 StopIteration을 발생시킨다.

__iter__()
    self를 반환한다. 그러면 for 루프 등 반복형이 필요한 곳에 반복자를 사용할 수 있게 해준다.
'''

'''
class Iterable:
    @abstractmethod
    def __iter__:
    
class Iterator(Iterable):
    __slots__ = ()
    
    @abstractmethod
    def __next__:
        raise StopIteration
    
    def __iter__(self):
        return self
    
    @classmethod
    def __subclasshook__(cls, c):
        if cls is Iterator:
            if (any("__next__" in B.__dict__ for B in C.__mro__) and
                any("__iter__" in B.__dict__ for B in C.__mro__)):
                return True
        
        return NotImplemented
'''
