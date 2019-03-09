# file: /python3.5/collections/__init__.py
# [참조] http://www.jinniahn.com/2016/07/ordereddict-python.html

from _weakref import proxy as _proxy

################################################################################
### OrderedDict
################################################################################

# dict에서 key의 list를 보여주는 클래스
class _OrderedDictKeysView(KeysView):

    # reversed()에 대해 대응하는 함수가 재정의되어 있다.
    def __reversed__(self):
        # 아래처럼 다른 list로 부터 yield로 가능하다.
        # yield from <list>
        yield from reversed(self._mapping)

# dict.items()에 했을 때 리턴되는데 객체
# 별도의 ItemsView를 상속 받고 있다.
class _OrderedDictItemsView(ItemsView):

    def __reversed__(self):
        # items는 ( key, value) 쌍으로 리턴된다.
        for key in reversed(self._mapping):
            yield (key, self._mapping[key])

# dict.values() 했을 때 리턴되는 데이터의 클래스
class _OrderedDictValuesView(ValuesView):

    def __reversed__(self):
        for key in reversed(self._mapping):
            yield self._mapping[key]

# OrderedDict에서 사용되는 item들을 liked 리스트로 만들어지는데
# 이때 link 객체가 쓰인다.
# __slots__는 객체를 만들때 기대되는 attr 목록이다. __slots__의
# 목적은 2가지
#    - 빠른 접근
#    - 메모리 절약
#
# @REF: http://stackoverflow.com/questions/472000/usage-of-slots
class _Link(object):
    __slots__ = 'prev', 'next', 'key', '__weakref__'

# 주목적 클래스다. dict에 기능을 더할 것이기 때문에 dict를 상속 받고 있다.
# OrderedDict는 입력되는 순서를 기억한다. 원래 dict는 내부의 구조에 따라서
# 입력되는 순서와 상관 없이 입력된 값을 빠르게 찾기 위해서 순서를 변경한다.
# 하지만 종종 dict와 같은면서 키의 순서도 유지 해야 하는 경우가 있다.
# 이럴 때 간단한 방법을 별로의 list를 만들어서 키만 저장하는 것이다.
# OrderedDict를 이런 과정을 좀 더 쉽게 하기 위한 것이다. 내가 상상 했던 것은
# 간단히 내부 list 객체가 있어서 key를 저장할 것이라고 생각했는데 뭔가
# 더 복잡하다. 왜 그런지 알아보자.
class OrderedDict(dict):
    'Dictionary that remembers insertion order'
    # An inherited dict maps keys to values.
    # The inherited dict provides __getitem__, __len__, __contains__, and get.
    # The remaining methods are order-aware.
    # Big-O running times for all methods are the same as regular dictionaries.

    # The internal self.__map dict maps keys to links in a doubly linked list.
    # The circular doubly linked list starts and ends with a sentinel element.
    # The sentinel element never gets deleted (this simplifies the algorithm).
    # The sentinel is in self.__hardroot with a weakref proxy in self.__root.
    # The prev links are weakref proxies (to prevent circular references).
    # Individual links are kept alive by the hard reference in self.__map.
    # Those hard references disappear when a key is deleted from an OrderedDict.

    # dict를 상속 받는다. dict는 __getitem__, __len__, __contains__, get등의
    # API를 제공한다. OrderedDict에서 제공하는 나머지는 순서를 고려한 함수들이다.
    # 모든 API의 시간복잡도(Big-O)는 기존 dict과 동일하다.

    # 내부 self.__map은 더블 링크드 리스트로 key 값을 보관한다. 왜 이렇게 했는지
    # 모르겠다. 그냥 list를 했으면 더 좋지 않았을까?
    # 어쨌던 "원형 더블 링크드 리스트"는 sentinel 엘리먼트로 시작점과 끝나는 점을
    # 보관한다. 이 엘리먼트는 삭제되지 않는다. 이 엘리먼트가 self.__hardroot이고
    # week proxy화 시켜서 __root에 저장한다. 말로 설명하기 힘들다. 이건 아래 코드에서
    # 확인하자. prev 링크가 약한 참조로 저장된다. 이것은 순환 참조를 막기 위한 것이다.
    # 원래 약한 참조의 목적대로...

    # 초기화 코드다. 다양한 파라미터에 대양하기 위해서 (*args, **kwds)로 설정했다.
    # OrderedDict(a=1,b=2,c=3)으로 넣으면 kwds에 dict로 저장되는데 이때 순서가
    # 사라지기 때문에 이런 방식으로 데이터를 넣는 것을 추천하지 않는다고 설명한다.
    # 그렇군
    def __init__(*args, **kwds):
        '''Initialize an ordered dictionary.  The signature is the same as
        regular dictionaries, but keyword arguments are not recommended because
        their insertion order is arbitrary.

        '''
        # 분명 상속을 했든데 부모 클래스의 __init__를 호출하지 않는다.
        # __init__은 self가 포함되니 애라 if not args 가 성립할 일이 없다.
        if not args:
            raise TypeError("descriptor '__init__' of 'OrderedDict' object "
                            "needs an argument")
        # 여시서 self와 args를 분리한다.
        # 그냥 초기 선언 부터 def __init__(self, *args, **kwds)라고 했으면 되지
        # 않았을까? 뭔가 다른 것이 있나???
        self, *args = args

        # 데이터가 좀 더 있어야 한다.
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))

        # 값 초기화 부분을 try~except로 처리했다. if로 처리해야 하지 않나
        # try~except를 예외를 위한 것이라고 생각하는데. 암튼 이런 것도
        # 있다.
        try:
            # 기존에 self.__root가 있으면 아무 일도 없고
            self.__root
        except AttributeError:

            # 초기화 한다.
            # key를 순서대로 저장하기 위한 sentinel 엘리먼트
            self.__hardroot = _Link()
            # __hardroot를 proxy로 만들든다.
            self.__root = root = _proxy(self.__hardroot)
            # prev, next로 자신을 가르키도록 일단 한다.
            # 이 리스트에 아이템을 추가하면 prev, next등을 변경할 거다.
            root.prev = root.next = root
            # __map이 뭐하는 거지???
            self.__map = {}

        # dict의 데이터를 위에서 받은 데이터로 넘긴다.
        # 이게 실질적인 부모클래스 초기화 코드가 된다.
        # 내 프로그램은 고정관점이 있었나보다. 이런 식으로도
        # 가능했다.
        self.__update(*args, **kwds)

    # a[key] = val 식으로 하면 아래 메소드가 호출된다.
    def __setitem__(self, key, value,
                    dict_setitem=dict.__setitem__, proxy=_proxy, Link=_Link):
        'od.__setitem__(i, y) <==> od[i]=y'
        # Setting a new item creates a new link at the end of the linked list,
        # and the inherited dictionary is updated with the new key/value pair.

        # 기존에 등록된 코드가 아니면
        if key not in self:
            # self.__map에 link를 저장한다.
            # 순서를 위한 link 객체
            # __map으로 키에 해당하는 Link를 찾고 그것을 기준으로
            # 앞, 뒤 모두를 접근할 수 있다.
            self.__map[key] = link = Link()

            # 여기서 링크드 리스트에 link를 삽입한다.
            # self.__root는 링크드 리스트의 시작과 끝을 모두 관리한다.
            # 위에서 설명한 데로 sentinel 엘리먼트로 사라지지 않는다.
            #
            # [root] --- [link1] --- [root]
            # [root] --- [link1] --- [link2] --- [root]
            #   ^          ^            ^
            #  root       last       (new link)
            root = self.__root
            last = root.prev

            link.prev, link.next, link.key = last, root, key  # last와 root 사에 link를 넣는다.
            last.next = link           # last 다음 새로운 링크가 추가된고
            root.prev = proxy(link)    # 다음번 turn에서 last가 된다.

        # 이게 원래 dict의 setitem이다.
        dict_setitem(self, key, value)

    # del od[y] 했을 때 호출됨
    # 근데 3번째 아이템은 원래 파라미터가 아니다.
    # 이런식의 호출이 가능했던가? 변수 선언을 파라미터 자리에 한 것이 아닌지?
    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        'od.__delitem__(y) <==> del od[y]'
        # Deleting an existing item uses self.__map to find the link which gets
        # removed by updating the links in the predecessor and successor nodes.

        # 원래 dict의 함수를 호출한다.
        dict_delitem(self, key)

        # double linked list 처리해야 한다. link 객체를 삭제해주어야 한다.
        # 일단 __map에서 제거한다.
        link = self.__map.pop(key)

        # 삭제된 링크의 point 데이터를 가져와서
        link_prev = link.prev
        link_next = link.next

        # 앞에 있는 link를 다시 연결해 둔다.
        link_prev.next = link_next
        link_next.prev = link_prev

        # 이건 왜 초기화 하지 어차피 사라질 텐데.??
        link.prev = None
        link.next = None

    # iter(od) 일 때 호출
    # iter를 만드는 방법을 보자.
    def __iter__(self):
        'od.__iter__() <==> iter(od)'
        # Traverse the linked list in order.

        # root의 다음 아이테이 첫번째다.
        root = self.__root
        curr = root.next

        # while은 종료시점이 조건식에 의해서 이루어진다.
        while curr is not root:

            # 아이템 하나 반환
            yield curr.key
            curr = curr.next

    # reversed(od)일 때 호출
    # 키를 뒤집는다. 여기서 double linked list를 한 보람이 나온다.
    def __reversed__(self):
        'od.__reversed__() <==> reversed(od)'
        # Traverse the linked list in reverse order.
        # __iter__에서는 next를 따라 갖는다. 여기서는 prev를 따라가면 된다.
        root = self.__root
        curr = root.prev
        while curr is not root:
            yield curr.key
            curr = curr.prev

    # 아이템들 제거
    def clear(self):
        'od.clear() -> None.  Remove all items from od.'
        # __map, __root를 초기화 시킨다.
        # 그리고 원래 dict 자료들도 제거한다.
        root = self.__root
        root.prev = root.next = root
        self.__map.clear()
        dict.clear(self)

    # od.popitem() 하면 앞에 있는 놈부터 나온다.
    # last가 True이면 뒷쪽
    def popitem(self, last=True):
        '''od.popitem() -> (k, v), return and remove a (key, value) pair.
        Pairs are returned in LIFO order if last is true or FIFO order if false.

        '''

        # 데이터가 비어 있으면 Exception
        if not self:
            raise KeyError('dictionary is empty')

        # self.__root가 길어서 그런지 항상 root로 다시 할당하고 있다.
        root = self.__root

        if last:
            # 뒤에서 뽑을때
            # root.prev는 항상 마지막이다.
            # 마지막 아이템을 제거한다.
            link = root.prev
            link_prev = link.prev
            link_prev.next = root
            # root.prev에 link.prev를 넣어서 리스트를 유지시킨다.
            root.prev = link_prev
        else:
            # 앞에서 뽑을 때
            # 에서 뽑을 때는 root와 link.next 아이템의 link를 수정해야 한다.
            link = root.next
            link_next = link.next
            root.next = link_next
            link_next.prev = root

        # link에 저장된 key를 뽑아서
        key = link.key
        # __map의 내용 제거하고
        del self.__map[key]
        # dict.pop으로 해당 item을 제거한다.
        value = dict.pop(self, key)
        return key, value

    # 기존 아이템을 처음에니 끝으로 이동시킨다.
    # 이건 왜 필요하지. LRU과 같이 최신에 뭔가하는 것을 유지 시키기 위해서
    # 아직까지 이렇게 할 이유는 없었는데.
    def move_to_end(self, key, last=True):
        '''Move an existing element to the end (or beginning if last==False).

        Raises KeyError if the element does not exist.
        When last=True, acts like a fast version of self[key]=self.pop(key).

        '''

        # 먼저 할 일을 작업하려는 item을 리스트에서 제거해야 한다.
        link = self.__map[key]
        link_prev = link.prev
        link_next = link.next
        link_prev.next = link_next
        link_next.prev = link_prev


        # 그리고 앞 혹은 뒤에 추가한다.
        # 순서와 관련된 것이므로 linked list 만 처리한다.
        root = self.__root
        if last:
            last = root.prev
            link.prev = last
            link.next = root
            last.next = root.prev = link
        else:
            first = root.next
            link.prev = root
            link.next = first
            root.next = first.prev = link

    # 메모리 크기를 반환한다. 순서를 유지시키기 위해서 추가한 자료구조 크기를
    # 다 포함시켜야 한다.
    # 근데 이건 왜 계산하는 거지??
    def __sizeof__(self):

        # C을 한 사람들에게는 sizeof 가 편하다.
        sizeof = _sys.getsizeof

        # 갯수는 root item을 포함하기 때문에 +1
        n = len(self) + 1                       # number of links including root

        # dict 사이즈에
        size = sizeof(self.__dict__)            # instance dictionary

        # 이 부분이 가장 이상 하다. __map은 link가 저장되는 dict인데..
        size += sizeof(self.__map) * 2          # internal dict and inherited dict
        # link 객체 사이트
        size += sizeof(self.__hardroot) * n     # link objects
        # proxy 객체 사이즈
        size += sizeof(self.__root) * n         # proxy objects

        # 최종 결과다.
        return size

    # dict의 부모 클래스의 update 메소스가 update로 쓰인다.
    update = __update = MutableMapping.update

    # d.keys()로 쓰일 때, 재미있는 것을 이때의 key로 순서가 유지된다는 점이다.
    # 이건 아마도 __iter__ 때문이지 않을까 생각한다. 디버깅은 하지 않았지만
    def keys(self):
        "D.keys() -> a set-like object providing a view on D's keys"
        return _OrderedDictKeysView(self)

    # d.items()
    def items(self):
        "D.items() -> a set-like object providing a view on D's items"
        return _OrderedDictItemsView(self)

    # d.values()
    def values(self):
        "D.values() -> an object providing a view on D's values"
        return _OrderedDictValuesView(self)

    # not is 처리
    __ne__ = MutableMapping.__ne__



    __marker = object()

    def pop(self, key, default=__marker):
        '''od.pop(k[,d]) -> v, remove specified key and return the corresponding
        value.  If key is not found, d is returned if given, otherwise KeyError
        is raised.

        '''
        if key in self:
            result = self[key]
            del self[key]
            return result
        # item도 없고 default 값이 주어지지 않으면 raise 발생
        # 위에서 선언한 __marker는 class member로 메모리 절약을 위한 기법
        # 사용자가 뭔가를 설정했지 알수 있는 방법
        if default is self.__marker:
            raise KeyError(key)
        return default

    # 기본값 설정
    # d.set(k,v)와 동일하나 기존에 값이 있으면 그대로 두고
    # 없으면 값을 설정한다. 옵션을 넘겨줄 때 편리하게 쓰겠다.
    def setdefault(self, key, default=None):
        'od.setdefault(k[,d]) -> od.get(k,d), also set od[k]=d if k not in od'

        # 기존 값이 있으면
        if key in self:
            return self[key]

        # 없으면 설정하고 리턴
        self[key] = default
        return default


    # repr로 생성된 스트링을 exec 시키면 그래도 동일한 데이터의 객체를 반환한다.
    @_recursive_repr()
    def __repr__(self):
        'od.__repr__() <==> repr(od)'
        if not self:
            return '%s()' % (self.__class__.__name__,)
        return '%s(%r)' % (self.__class__.__name__, list(self.items()))

    # 내부의 데이터를 정리한다.
    def __reduce__(self):
        'Return state information for pickling'

        # 내부 __dict__를 복사한다.
        inst_dict = vars(self).copy()
        #
        for k in vars(OrderedDict()):
            # exception 반환을 위해서 기본 값 설정
            inst_dict.pop(k, None)

        # 정리된 데이터를 반환한다.
        return self.__class__, (), inst_dict or None, None, iter(self.items())

    # 얇은 복사
    def copy(self):
        'od.copy() -> a shallow copy of od'
        # 다시 생성해서 복사한다.
        return self.__class__(self)

    # 주어진 데이터로 만든다. 객체를 만든다. factory pattern 같은
    @classmethod
    def fromkeys(cls, iterable, value=None):
        '''OD.fromkeys(S[, v]) -> New ordered dictionary with keys from S.
        If not specified, the value defaults to None.

        '''
        # 객체 생성해서
        self = cls()
        for key in iterable:
            # 값을 하나 하나 입력한다.
            self[key] = value
        return self

    # 값을 객체인지 확인
    def __eq__(self, other):
        '''od.__eq__(y) <==> od==y.  Comparison to another OD is order-sensitive
        while comparison to a regular mapping is order-insensitive.

        '''
        # OrderedDict 이면
        if isinstance(other, OrderedDict):
            # 내용도 확인하고 순서도 확인한다.
            return dict.__eq__(self, other) and all(map(_eq, self, other))
        # 아니면 내용이 같은지 확인한다
        return dict.__eq__(self, other)


# 다른 모듈(더빠른)에서 구현된 OrderedDict가 있으면
# 그것을 로드한다. 위에서 설명한 것은 그것이 없을 때 순수 python으로 작성한 것
try:
    from _collections import OrderedDict
except ImportError:
    # Leave the pure Python version in place.
    pass