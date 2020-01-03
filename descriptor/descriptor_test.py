from types import FunctionType

def user_func():
    pass

print(id(user_func))
print(user_func)
print(vars(user_func))
print(dir(user_func))
print(user_func.__get__)
print(type(user_func))

#print(str.__dict__)
#print(dir(str))