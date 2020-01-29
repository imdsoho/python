import sys

'''a = 'hello'
b = 'my name'
c = 'imdsoho'
print(a, b, c, sep=':')'''

# print(*objects, sep=' ', end='\n', file=sys.stdout)
# Print objects to the stream file, separated by sep and followed by end.
# sep, end and file, if present, must be given as keyword arguments.

#print(sys.version_info)

def ilaya1():
    print(sys._getframe())
    print(sys._getframe().f_code)
    current_func_name = sys._getframe().f_code.co_name
    print ("{}".format(current_func_name))


if __name__ == "__main__":
    ilaya1()
