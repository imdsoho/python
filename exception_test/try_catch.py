import json

handle = open("D:/var/lawfile.txt")
try:
    data = handle.read()
finally:
    handle.close()

#print(data)

def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]

string_json = '{"id":"12345", "state":"Y", "remark":"good"}'
state = load_json_key(string_json, "state")
print(state)



def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('invalid inputs') from e

x, y = 0, 2
try:
    result = divide(x, y)
except ValueError:
    print('invalid inputs')
else:
    print('result % 1.f' % result)

def divide2(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        return None

x, y = 0, 5
result = divide2(x, y)
print(result)
if not result:
    print("ERROR")