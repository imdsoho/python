def gen_123():
    # 일반적으로 제너레이터 함수 안에는 루프가 있지만, 꼭 그래야 하는 것은 아니다.
    # yield 키워드를 3번 사용했다.
    yield 1
    yield 2
    yield 3

def call_gen_123():
    print("id: ", gen_123)

    print("method call: ", gen_123())

    # 제너레이터는 yield에 전달된 표현식의 값을 생성하는 반복자다.
    for i in gen_123():
        print("value : ", i)

    # g는 반복자이므로 (__next__() 구현) next()를 호출하면 yield가 생성한 다음 항목을 가져온다.
    # 함수 본체가 반환될 때 이 함수를 포함하고 있는 제너레이터 객체는 Iterator 프로토콜에 따라서 StopIteration 예외를 발생
    g = gen_123()
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

def gen_AB():
    print('start')
    yield 'A'
    print('continue')
    yield 'B'
    print('end')

def call_gen_AB():
    for c in gen_AB():
        print('---> ', c)
        print("--------")

if __name__ == '__main__':
    call_gen_AB()
