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


