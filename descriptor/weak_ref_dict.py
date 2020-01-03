from weakref import WeakKeyDictionary
from typing import Callable

class DescriptorClass:
    def __init__(self, init_value):
        self.value = init_value
        self.mapping = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.mapping.get(instance, self.value)

    def __set__(self, instance, value):
        self.mapping[instance] = value



class SharedDataDescriptor:
    def __init__(self):
        self.name = None

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.value

    def __set__(self, instance, value):
        self.value = value

    def __set_name__(self, owner, name):
        self._name = name

class ClientClass:
    aa = SharedDataDescriptor()
    print(type(aa))

    def __init__(self, aa):
        self.username = aa



c1 = ClientClass("1st data")
#print(c1.username)

#c2 = ClientClass()
#print(c2.descriptor)

#c2.descriptor = "CHANGE"
#print(c1.descriptor)
#print(c2.descriptor)


class CallableClassTest():
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    #def __call__(self, *args, **kwargs):
    #    pass

call = CallableClassTest()
print(callable(call))

