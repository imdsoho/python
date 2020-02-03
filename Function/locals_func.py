#URL: https://charsyam.wordpress.com/2018/05/03/%EC%9E%85-%EA%B0%9C%EB%B0%9C-%EC%8B%A0%EB%AC%98%ED%95%9C-python-locals-%EC%9D%98-%EC%84%B8%EA%B3%84/

global_var = 'GLOBAL'

def locals_test(x):
    locals()['v'] = x + 10
    #print(type(locals()))
    print("1: ", locals())
    locals()['x'] = 0
    print("2: ", x)
    x = 0
    print("3: ", x)
    print("4: ", locals())
    locals()['v'] = x + 10
    print("5: ", locals())

    #print("6: ", v)        # ERROR
    return locals()['v']    # OK


def globals_test(g):
    print(type(globals()))

    for data in globals():
        print(data, " : ", globals()[data])

param = 100
globals_test(param)
