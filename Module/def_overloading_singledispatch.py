from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(obj)
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
# 특화된 함수의 이름은 필요 없으므로 언더바로 함수명을 지정한다.
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<pre>{0}</pre>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0.x})</pre>'.format(n)

# 가능하면 int나 list와 같은 구상 클래스보다
# numbers.Integral, abc.MutableSequence와 같은 추상 베이스 클래스를 처리하도록
# 특화된 함수를 등록하는 것이 좋다.
@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n</i>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
