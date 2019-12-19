def generator():
    yield 1
    yield 2
    return 3

value = generator()

try:
    print(next(value))
    print(next(value))
    data = next(value)
except StopIteration as e:
    print(e)


