import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # 반복형 구현 명시
    # 반복자 객체를 생성해서 반환함으로써 반복형 프로토콜 구현
    def __iter__(self):
        return SenteenceIterator(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

# 반복자는 __next__()와 __iter__() 메서드를 모두 구현해야 한다.
# 둘 다 구현하면 issubclass(SentenceIterator, abc.Iterator) 테스트를 통과
class SenteenceIterator:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index += 1
        return word

    def __iter__(self):
        return self


if __name__ == "__main__":
    s = Sentence('"The time has come, "the Walrus said, time is important.')
    print(s)

    for word in s:
        print(word)

    list = list(s)
    print(list)
