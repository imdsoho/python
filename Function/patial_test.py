from functools import partial

print(type(partial))

def add(a, b):
    return a + b

add_one = partial(add, "a")

#print(type(add_one))
#print(add_one)
print(add_one("b"))

class PartialTest():
    def __init__(self, name):
        self.name = name

    '''def __str__(self):
        return self.name'''

wrap = partial(PartialTest, "jsc")

data = wrap()
print(data)

test = PartialTest("name")

print(callable(PartialTest))
print(callable(test))
