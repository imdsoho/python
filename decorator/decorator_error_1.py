from functools import wraps

def trace_decorator(function):
    def custome_wrapped(*args, **kwargs):
        print("%s 실행 ", function.__qualname__)

        return function(*args, **kwars)

    return custome_wrapped

def trace_decorator_wraps(function):
    @wraps(function)
    def custome_wrapped(*args, **kwargs):
        print("%s 실행 ", function.__qualname__)

        return function(*args, **kwars)

    return custome_wrapped


#@trace_decorator
@trace_decorator_wraps
def process_account(account_id):
    '''
    print("%s 계정 ", account_id) 
    '''

help(process_account)
print("-------------------")
print(process_account.__qualname__)
print("-------------------")
print(process_account.__wrapped__)

'''
Help on function custome_wrapped in module __main__:
custome_wrapped(*args, **kwargs)
-------------------
trace_decorator.<locals>.custome_wrapped
'''

'''
Help on function process_account in module __main__:
process_account(account_id)
    print("%s 계정 ", account_id)
-------------------
process_account
'''






