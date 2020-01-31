import weakref

class Apple:
    pass

def callback(reference):
    print('callback({!r})'.format(reference))

apple = Apple()
apple.color = 'red'

r = weakref.ref(apple, callback)
print(type(r), r)

ref_a = r()
print(apple.color)
print(ref_a.color)
print(apple is ref_a)

del apple
