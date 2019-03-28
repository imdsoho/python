import sys

# sys._getframe().f_locals

def customsub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

name = 'Guido'
n = 37
s = '{name} has {n} messages'

# __missing__() 메소드가 있는 딕셔너리 클래스 정의
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
formatings = s.format_map(safesub(vars()))
print(formatings)

print(customsub('Hello {name}'))
print(customsub('Your favorite color is {color}'))
