class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print("Here's My int", args)
        print("Now do whatever you want with thers objects.")
        return type.__call__(cls, *args, **kwargs)

class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y

i = int(4,5)
print(i)