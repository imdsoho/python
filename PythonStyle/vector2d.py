from array import array
import math

class Vector2d:
    # __slots__ 를 정의하면 '이 속성들이 이 클래스가 가지는 속성' 임을 인터프리터에게 알려준다.
    # __slots__ 속성은 파이썬 인터프리터가 객체 속성을 딕셔너리 대신 튜플에 저장한다.
    __slots__ = ('__x', '__y')

    typecode = 'd'

    def __init__(self, ix, iy):
        self.__x = float(ix)
        self.__y = float(iy)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{} ({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(array(self.typecode, self)))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cla(*memv)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        print("abs call")
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == "__main__":
    v1 = Vector2d(3,4)

    #v1_clone = eval(repr(v1))
    #print(repr(v1))

    #print(abs(v1))
    #print(bool(v1))

    #print(v1.x)

    #print(v1.__dict__)

    # getter()를 사용하여 값을 보호한다. @property
    #v1.x = 0   # ERROR 발생 - 불변형 객체
    # print(v1)

