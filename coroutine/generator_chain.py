def chain(*iterables):
    for it in iterables:
        for value in it:
            yield value

def chain_from(*iterables):
    for it in iterables:
        yield from it

'''data = list(chain("hello", ["world"], ("tuple", "of", "values")))
print(data)

data2 = list(chain_from("hello", ["world"], ("tuple", "of", "values")))
print(data)'''

def sequence(name, start, end):
    print("%s started at %i", name, start)
    yield from range(start, end)
    print("%s finished at %i", name, end)
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
print(next(g))
print(next(g))
print(next(g))
