'''
딕셔너리는 키와 값의 매핑으로 이루어진다.

딕셔너리의 keys() 메소드는 키를 노출하는 key-view 객체를 반환한다.

키뷰에는 합집합, 교집합, 여집합 같은 집합 연산 기능이 있다.

a.keys() & b.keys() # 동일한 키 찾기

a.keys() - b.keys() # a에만 있고 b에는 없는 키 찾기

a.items() & b.items() # (키, 값)이 동일한 것 찾기

딕셔너리의 items() 메소드는 (key, value) 페어로 구성된 아이템-뷰 객체를 반환한다.

values() 메소드는 집합 연산을 지원하지 않는다.
'''

a = {
    'x':1,
    'y':2,
    'z':3
}

b = {
    'w':10,
    'x':11,
    'y':2
}

c = { key:a[key] for key in a.keys() - {'x', 'w'}}

#print (c)

def dedupe(items, key=None):
    seen = set()

    #print (type(key))

    for item in items:
        print ("1", item, key(item))

        val = item if key is None else key(item)

        if val not in seen:
            yield item
            seen.add(val)

alist = [{'x':1, 'y':2}, {'x':1,'y':3}, {'x':1, 'y':2}, {'x':2,'y':4}]

seen = list(dedupe(alist, key=lambda d: (d['x'], d['y'])))

print (seen)


