import re

line = 'asdf fjdk; afed, fjek,asfd,   foo'
wlist = re.split(r'[;,\s]\s*', line)
#print(type(wlist))

# re.split() 을 사용할 때는 괄호 안에 묶인 정규 표현식 패턴이 캡처 그룹이 된다.
# 캡처 그룹을 사용하면, 매칭된 텍스트에도 결과가 포함

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

values = fields[::2]
delimiters = fields[1::2]+['']

print(values)
print(delimiters)

# 분리 구문을 결과에 포함시키고 싶지 않지만 정규 표현식에 괄호를 사용해야하면 논캡처 그룹을 사용한다.
# (?:...) 와 같이 사용하면 된다.
nonlist = re.split(r'(?:,|;|\s)\s*', line)
print(nonlist)

# match()는 항상 문자열 처음에서 찾기를 시도한다. (문자열의 처음만 확인한다.)
# 텍스트 전체에 걸쳐 패턴을 찾으려면 findall() 메소드를 사용한다.
url = 'http://www.python.org'
if re.match(r'http|https|ftp', url):
    print(re.match(r'http|https|ftp', url))
    print('MATCH')
else:
    print('NON')

text1 = '11/27/2012'
datepart = re.compile(r'\d+/\d+/\d+')
if datepart.match(text1):
    print('YES')
else:
    print('NO')

long_text = 'Today is 11/27/2012, PyCon starts 3/13/2013'
mlist = datepart.findall(long_text)
print(mlist)

# 패턴을 명시할 때 r'(\d+)/(\d+)/(\d+) 와 같이 로우 문자열을 그대로 쓰는 것이 일반적이다.
# 로우 문자열을 사용하지 않으면 '(\\d+)/(\\d+)/(\\d+)와 같이 \\를 두번 사용해야 한다.
groupdatepat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = groupdatepat.match('11/27/2012')
print('0: ', m.group(0))
print('1: ', m.group(1))
print('2: ', m.group(2))
print('3: ', m.group(3))
print('all: ', m.groups())

gm = groupdatepat.findall(long_text)
print(gm)
for month, day, year in groupdatepat.findall(long_text):
    print('{}-{}-{}'.format(year, month, day))

rlist = re.sub(groupdatepat, r'\1-\2-\3', long_text) # Today is 11-27-2012, PyCon starts 3-13-2013
#rlist = re.sub(groupdatepat, r'\3-\1-\2', long_text) # Today is 2012-11-27, PyCon starts 2013-3-13
print('replace: ', rlist)
# 숫자 앞에 백슬래스가 붙어 있는 \3과 같은 표현은 패턴의 캡처 그룹을 참조한다.

# 복잡한 치환의 경우, 콜백을 사용할 수 있다.
from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

clist = groupdatepat.sub(change_date, long_text)
print('callback: ', clist)

from fnmatch import fnmatch, fnmatchcase
# 파일 이름뿐만 아니라 데이터 프로세싱(데이터 처리)에도 사용된다

# 운영체제의 대소문자 규칙을 따른다. (Mac - 대소문자 구분, Windows - 구분하지 않음)
bRet = fnmatch('foo.txt', '*.txt')
print(bRet)

names = ['data1.csv', 'data2.csv', 'config.ini', 'foo.py']
nlist = [name for name in names if fnmatch(name, 'data*.csv')]
print(nlist)

# 소문자, 대문자를 구분한다
fnmatchcase('foo.txt', '*.TXT')
# False

address = [
    '1234 CLARK ST', '12 ADDISON ST', '78 GAANVILLE AVE'
]

alist = [addr for addr in address if fnmatch(addr, '* ST')]
print(alist)

# 대소문자를 구분하지 않고 검색하기
text = "UPPER PYTHON, lower python, Mixed Python"
re.findall('python', text, flags=re.IGNORECASE)
re.sub('python', 'snake', text, flags=re.IGNORECASE)

def matchcase(word):

    def replace(m):
        text = m.group()

        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word

    return replace

chgText = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(chgText)

# 가장 짧은 매칭을 위한 정규 표현식
str_pat = re.compile(r'/"(.*)/"')
text1 = 'Computer says "no."'
str_pat.findall(text1)

text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2)

str_pat2 = re.compile(r'/"(.*?)/"')
str_pat2.findall(text2)

