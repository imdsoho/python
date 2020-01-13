from functools import wraps
import logging
from inspect import signature

def logged(level, name=None, message=None):
    print("[1]")
    def decorate(func):
        print("[2]")
        print(signature(func))

        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        #print("[name : ",  logname, "], [msg : ", logmsg, "]")

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("[3]")
            log.log(level, logmsg)

            print("[4]")
            return func(*args, **kwargs)

        print("[5]")
        return wrapper

    print("[6]")
    return decorate

@logged(logging.DEBUG)
def add(x, y):
    return x+y

#@logged(logging.CRITICAL, name='example', message='default log message')    # [name :  example ], [msg :  default log message ]
#@logged(logging.CRITICAL, name='example')           # [name :  example ], [msg :  spam ]
'''@logged(logging.CRITICAL, 'example')               # [name :  example ], [msg :  spam ]
def spam():
    return "Spam!"
'''

print("------------------------")
print("add() : " , add(1,2))
#print("spam() : ", spam())
