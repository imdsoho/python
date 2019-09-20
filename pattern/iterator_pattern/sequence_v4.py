import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, text):
        self.text = text
        # 조급한 계산법
        # 사용하지 않아도 객체 생성시 필요한 데이터를 모두 생성
        #self.words = RE_WORD.findall(text)

    def __iter__(self):
        # 느긋한 계산법
        for match in RE_WORD.finditer(self.text):
            yield match.group()

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
