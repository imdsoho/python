'''
OrderedDict는 내부적으로 더블 링크드 리스트(doubly linked list)로 삽입 순서와 관련 있는 키를 기억한다.

새로운 아이템을 처음으로 삽입하면 리스트의 제일 끝에 위치시킨다.

더블 링크드 리스트를 사용하기 때문에 OrderedDict의 크기는 일반적인 딕셔너리에 비해 두 배로 크다.

popitem(last=True) OrderedDict의 아이템들을 반환 및 삭제하는 메소드

last=True인 경우, LIFO(Last In Last Out)방식으로 값을 반환 및 삭제

move_to_end(key, last=True) 맨 오른쪽(뒤) 또는 맨 왼쪽(앞)으로 이동해주는 메소드

last=True인 경우, 맨 오른쪽(뒤)로 이동하고, False인 경우, 맨 왼쪽(앞)으로 이동한다.
'''

