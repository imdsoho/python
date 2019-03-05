from collections import defaultdict

d1 = defaultdict(object)
d2 = defaultdict(lambda : 0)
d2["a"] = "one"

for key in d2:
    print "%s, %s" % (key, d2[key])


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
print list(d.items())





