class CustomException(Exception):
    """A type of exception that is under control."""


def sequence(name, start, end):
    value = start
    print("%s started at %i", name, value)
    while value < end:
        try:
            received = yield value
            print("%s received %r", name, received)
            value += 1
        except CustomException as e:
            print("%s is handling %s", name, e)
            received = yield "OK"
    return end


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)
    return step1 + step2

g = main()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
#print(next(g))
