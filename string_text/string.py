import os
import re

filenames = os.listdir('.')
flist = [name for name in filenames if name.endswith(('.c','.h'))]
print(flist)

# 튜플 만을 입력으로 받는다. 리스트나 세트를 가지고 있다면 tuple()을 사용해서 변환해야 한다.
choices = ['http', 'ftp']
url = 'http://www.python.org'
url.startswith(tuple(choices))

matchBool = re.match('http|https|ftp', url)
print(matchBool)

# str.startswith()
# str.endswith()
# str.find()
# str.replace()

# 문자열에서 문자 잘라내기
#str.strip()
#str.lstrip()
#str.rstrip()
stripstr = '------hello====='
print(stripstr.strip('-='))

filename = './regularExpress.py'
with open(filename) as f:
    lines = (line.strip() for line in f)

    for line in lines:
        #print(line)
        pass

# 문자열 합치기
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)
','.join(parts)

a = 'Is Chicago'
b = 'Not Chicago'
sum = '{} {}'.format(a, b)
print(sum)

# + 연산자로 많은 문자열을 합치려고 하면 메모리 복사와 가비지 컬렉션으로 인해 매우 비효율적이다.
# += 연산자는 새로운 문자열 객체를 만들어낸다.

data = ['ACME', 50, 91.1]
sumdata = ','.join(str(d) for d in data)
print(sumdata)

def sample():
    yield 'IS'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

text = ' '.join(sample())

for part in sample():
    # f.write(part)
    pass

# 문자열에 변수 사용
s = '{name} has {n} messages'
formatings = s.format(name='Guido', n=37)
print(formatings)

name = 'Guido'
n = 37
formatings = s.format_map(vars())
print(formatings)

# __missing__() 메소드가 있는 딕셔너리 클래스 정의
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
formatings = s.format_map(safesub(vars()))
print(formatings)

import sys
def customsub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

print(customsub('Hello {name}'))
print(customsub('Your favorite color is {color}'))

