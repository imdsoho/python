import weakref

class Apple:
    pass

a = Apple()
a.color = 'red'

r = weakref.ref(a)
print(type(r), r)

ref_a = r()
print(a.color)
print(ref_a.color)
print(a is ref_a)


