# defaultdict은 dictionary에 기본값을 정의하고 키 값이 없더라도 에러가 나지 않고, 기본값을 반환한다.
'''
d = defaultdict(object)
d = defaultdict(labda:0)
s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dd = defaultdict(int)
for k in s:
dd[k] += 1
print(dict(dd))
'''

# setdefault는 키값과 값 하나를 인자로 받는 dict의 메소드

'''
s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
d= {}
for k in s:
d.setdefault(k,0)
d[k]+=1
print list(d.items())
'''

from collections import defaultdict

d1 = defaultdict(object)
d2 = defaultdict(lambda : 0)
d2["a"] = "one"

for key in d2:
    print ("%s, %s") % (key, d2[key])


s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
dd = defaultdict(int)
for k in s:
    dd[k] += 1
print(dict(dd))


s= ['a', 'b', 'c', 'b', 'a', 'b', 'c']
d= {}

for k in s:
    d.setdefault(k,0)
    d[k]+=1
print (list(d.items()))





