iter = (x for x in range(10))

print(iter)
print(next(iter))
print(next(iter))

roots = ((x, x**0.5) for x in iter)

print(next(roots))
print(next(roots))

print(next(iter))
print(next(roots))