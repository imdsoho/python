with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:   # 순환의 끝을 나타냄
        pass

with open('/etc/passwd') as f:
    while True:
        # Return the next item from the iterator. If default is given and the iterator
        # is exhausted, it is returned instead of raising StopIteration.
        line = next(f, None)
        if line is None:
            break
        print(line, end='')


