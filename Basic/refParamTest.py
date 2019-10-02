
list_param = ['1','2','3']
str_param = "string"
dict_param = {"key": str_param}
tuple_param = ('a', 'b')
int_param = 0

def send_func():
    receive_func(list_param, str_param, dict_param, tuple_param, int_param)

def receive_func(lparam, sparam, dparam, tparam, iparam):
    str_save = sparam
    tuple_save = tparam
    int_save = iparam
    dict_save = dparam.copy()   # 가변 객체
    list_save = lparam.copy()   # 가변 객체

    sparam = "None"
    tparam = ('0','0')
    iparam = -1
    dparam['key'] = "_blank"
    lparam[0] = 'A'

    print(" [S-ORIGIN] " + str(str_save) + "\t\t\t\t [S-CHANGE] " + str(sparam) + "\t\t\t\t [S-AFTER] " + str(str_param))
    print(" [T-ORIGIN] " + str(tuple_save) + "\t\t\t [T-CHANGE] " + str(tparam) + "\t\t\t [T-AFTER] " + str(tuple_param))
    print(" [I-ORIGIN] " + str(int_save) + "\t\t\t\t\t [I-CHANGE] " + str(iparam) + "\t\t\t\t\t [I-AFTER] " + str(int_param))
    print(" [L-ORIGIN] " + str(list_save) + "\t\t [L-CHANGE] " + str(lparam) + "\t\t [L-AFTER] " + str(list_param))
    print(" [D-ORIGIN] " + str(dict_save) + "\t [D-CHANGE] " + str(dparam) + "\t [D-AFTER] " + str(dict_param))

send_func()



