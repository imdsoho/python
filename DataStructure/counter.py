from collections import Counter

words = ['look','into','my','eyes','look','into','my','eyes','the','eyes','the','eyes','not','around',
         'the','eyes',"don't",'look','around','the','eyes','look','into','my','eyes',"you're",'under']

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# Counter 객체에는 해시 가능한 모든 아이템을 입력할 수 있다.

# Counter 인스턴스의 기능 중 여러 수식을 사용할 수 있다.

morewords = []

a = Counter(words)
b = Counter(morewords)
c = a + b
d = a - b
