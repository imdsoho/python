import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    # 제너레이터
    # 메서드 호출 시 자동으로 제너레이터를 생성한다.
    def __iter__(self):
        for word in self.words:
            yield word

        return

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)


if __name__ == "__main__":
    s = Sentence('"The time has come, "the Walrus said, time is important.')
    print(s)

    for word in s:
        print(word)

# 본체 안에 yield 키워드를 가진 함수는 모두 제너레이터 함수이다.
# 제너레이터 함수는 호출되면 제너레이터 객체를 반환한다.
# 제너레이터 함수는 제너레이터 팩토리라고 할 수 있다.
