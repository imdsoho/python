import array

numbers = array.array('h', [-2, -1, 0, 1, 2])
print(numbers)
print(id(numbers))

memv = memoryview(numbers)
#print(len(memv))
print(id(memv))

memv_oct = memv.cast('B')
print(id(memv_oct))