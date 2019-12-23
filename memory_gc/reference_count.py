import sys

class ClassObject:
    pass

def functionObject_1():
    pass

def functionObject_2():
    pass

def show_ref_count():
    str_obj = "string_data"
    print("str : ", sys.getrefcount(str_obj))

    dict_obj = {"a":"1", "b":2}
    print("dict : ", sys.getrefcount(dict_obj))

    tuple_obj = (1,2,3,"a","b")
    print("tuple : ", sys.getrefcount(tuple_obj))

    set_obj = {"a", "b", "c"}
    print("set : ", sys.getrefcount(set_obj))

    arr_obj = [1,2,3]
    print("arrary : ", sys.getrefcount(arr_obj))

    cls_obj = ClassObject()
    print("class : ", sys.getrefcount(cls_obj))

    print("func-1 : ", sys.getrefcount(functionObject_1))

    func_obj = functionObject_2()
    print("func-2 : ", sys.getrefcount(func_obj))

show_ref_count()

