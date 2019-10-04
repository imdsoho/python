class Entity:
    def __init__(self, size, x, y):
        self.x, self.y = x,y
        self.size = size

    def __call__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return "[X] : " + str(self.x) + "[Y] : " + str(self.y)


def call_back_func(callback, *args):
    print(type(callback))

    if len(args) == 2:
        callback(args[0], args[1])
    else:
        raise AttributeError("argument lenth error")

entity = Entity(0,0,0)
print(entity)

#entity(1,1)

call_back_func(entity, 1, 1, 2)
print(entity)

