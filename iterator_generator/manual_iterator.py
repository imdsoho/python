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


# 순환 가능한 객체를 담은 사용자 정의 컨테이너 생성
# 사용 가능한 iterator 생성 방법
# __iter__() 메소드 정의

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        # iter() built-in method
        #     iter(iterable) -> iterator
        #     iter(callable, sentinel) -> iterator
        #
        #     Get an iterator from an object.
        #     In the first form, the argument must supply its own iterator, or be a sequence.
        #     In the second form, the callable is called until it returns the sentinel.
        return iter(self._children)

    def depth_first(self):
        #print('[1]', self)
        yield self

        for c in self:
            #print('[2]', self)
            yield from c.depth_first()



def frange(start, stop, increment):
    data = []

    def loopfunc(start, stop, increment):
        x = start
        while x < stop:
            yield x
            x += increment

    cgen = loopfunc(start, stop, increment)
    print(cgen)
    # <generator object frange at 0x123456789>
    # 제너레이터 함수가 반환되면 순환을 종료한다.

    #for n in loopfunc(start, stop, increment):
    # 아래와 동일한 기능
    for n in cgen:
        data.append(n)

    return data

def cookfrange(start, stop, incremet):
    x = start
    while x < stop:
        # yield 문의 존재로 인해 함수가 제너레이터가 되었다.
        yield x
        x += incremet

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for ch in root:
        print(ch)

    deligate = iter(root)
    print(next(deligate))

    x = [1,2,3]
    #print(next(x))
    xiter = iter(x)
    print(next(xiter))

    # [1]
    cooklist = list(cookfrange(0, 4, 1))
    print(cooklist)

    # [1]과 같은 결과 - list() 함수를 사용하지 않음
    datalist = frange(0, 4, 1)
    print(datalist)

    for ch in root.depth_first():
        #print(ch)
        pass


    # 역방향 순환
    # 객체가 __reversed__() 메소드를 구현하거나, 크기를 알 수 있는 경우만 가능
    # 그렇지 않으면 먼저 list로 변환해야 한다.
    f = open('/etc/passwd')
    for line in reversed(list(f)):
        #print(line, end='')
        pass

    countdown = Countdown(5)
    reversedcount = reversed(countdown)
    #print("[R] ", reversed(countdown))

    for n in reversedcount:
        print('[count] ', n) # 1, 2, 3, 4, 5

    itercount = iter(countdown)
    for n in itercount:
        print("[N] ", n)    # 5, 4, 3, 2, 1
