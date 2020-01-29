from multiprocessing import Pool, TimeoutError
import time
import os
import multiprocessing as mp

def f(x):
    return x*x

if __name__ == '__main__':
    mp.set_start_method('spawn')

    # 4개의 작업자 프로세스를 시작합니다
    with Pool(processes=4) as pool:

        # "[0, 1, 4,..., 81]" 를 인쇄합니다
        print(pool.map(f, range(10)))
        print("1---------------------")

        # 같은 숫자를 임의의 순서로 인쇄합니다
        for i in pool.imap_unordered(f, range(10)):
            print(i)
        print("2---------------------")

        # "f(20)" 을 비동기적으로 평가합니다
        res = pool.apply_async(f, (20,))      # *오직* 하나의 프로세스에서 실행합니다
        print(res.get(timeout=1))             # "400" 을 인쇄합니다
        print("3---------------------")

        # "os.getpid()" 를 비동기적으로 평가합니다
        res = pool.apply_async(os.getpid, ()) # *오직* 하나의 프로세스에서 실행합니다
        print(res.get(timeout=1))             # 그 프로세스의 PID 를 인쇄합니다
        print("4---------------------")

        # 여러개의 평가를 비동기적으로 수행하면 더 많은 프로세스를 쓸 *수* 있습니다
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])
        print("5---------------------")

        # 한 작업자를 10초간 잠자게 합니다
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("인내심이 부족해서 multiprocessing.TimeoutError 를 얻었습니다")

        print("잠시 동안, 풀을 다른 작업에 사용할 수 있습니다")

    # 'with'-블록을 빠져나가면 풀이 중단됩니다
    print("이제 풀이 닫혔고 더는 사용할 수 없습니다")