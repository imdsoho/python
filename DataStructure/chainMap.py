# ChainMap은 매핑을 여러 개 받아서 하나처럼 보이게 한다.
# 매핑에 대한 리스트를 유지하면서 리스트를 스캔하도록 일반적인 딕셔너리 동작을 재정의
# 중복키가 있으면 첫번째 매핑의 값을 사용

from collections import ChainMap
a = {'x':1, 'z':2}
b = {'y':2, 'z':3}
c = ChainMap(a, b)
#print (len(c)) # 3

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
#print(values)

# 완전히 별개의 딕셔너리를 생성하여 하나로 합친다.
# 원본 딕셔너리의 내용을 변경해도 합쳐 놓은 딕셔너리에 영향은 없다.
merged = dict(a)
print(merged)
print(a)
#print(c)
print("------------")

merged['x'] = '@'
a['x'] = 'A'
print(merged)
print(a)
#print(c)

print("------------")
merged.update(a)
#print (len(merged)) # 3
print(merged)
print(a)
#print(c)
# 원본 dictionary의 변경 내용은 반영되지 않는다.
# update() - 원본 딕셔너리의 변경을 반영한다.
