__all__ = ['deque', 'defaultdict', 'namedtuple', 'UserDict', 'UserList',
            'UserString', 'Counter', 'OrderedDict', 'ChainMap']

from _collections_abc import *
import _collections_abc
__all__ += _collections_abc.__all__

from _collections import deque
