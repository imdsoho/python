import sys

class Foo():
    def __init__(self):
        self.x = "A"
    pass

a = Foo()
b = Foo()

#print("[A]",  id(a), sys.getrefcount(a))
#print("[B]",  id(b), sys.getrefcount(b))

a.x = b
b.y = a

#print("[A]",  id(a), sys.getrefcount(a))
print("[B]",  id(b), sys.getrefcount(b))


#del a.x
print("[A]",  id(a), sys.getrefcount(a))
print("[A.x]",  id(a.x), sys.getrefcount(a.x))
print("[B.y]",  id(b.y), sys.getrefcount(b.y))
