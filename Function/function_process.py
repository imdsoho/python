from types import MethodType

class Method:
    def __init__(self, name):
        self.name = name

    def __call__(self, instance, arg1, arg2):
        print(f"{self.name} : {instance} call. {arg1}, {arg2}")

    def __get__(self, instance, owner):
        if instnace is None:
            return self

        return MethodType(self, instnace)

    def class_method(self):
        pass

class MyClass:
    method = Method("internal call")

instnace = MyClass()
Method("External call")(instnace, "first", "second")
instnace.method("first", "second")

print(type(Method.class_method))

class Coordinate2D:
    __slots__ = ("lat", "long")

    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def __repr__(self):
        return f"{self.__class__.__name__} {self.lat} {self.long}"

coord = Coordinate2D(1,1)
print(">" , dir(coord))
print(">>" , vars(coord))