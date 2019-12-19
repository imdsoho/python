class Position:
    def __init__(self, value):
        self.value = value
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.value

    def __set__(self, instance, value):
        self.value = value

class Grid:
    #x = Position("pos_x")
    #y = Position("pos_x")

    def __init__(self):
        #pos_x = Position("pos_x")
        #pos_y = Position("pos_x")
        #self.x = pos_x
        #self.y = pos_y

        self.x = Position("pos_x")
        self.y = Position("pos_y")

    def __str__(self):
        return "[x, y] = [%s, %s]" % (x, y)


grid1 = Grid()
#print(grid1.x.value)
#print(grid1.__dict__)
print(grid1.x)

'''grid1.x = 1
grid1.y = 1
print(grid1.x.value)    # error'''

'''grid2 = Grid()
print(grid2.y.value)
grid2.x = 2
grid2.y = 2
print(grid1.y.value)    # error'''


