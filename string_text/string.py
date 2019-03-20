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
