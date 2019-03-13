prices = {'A':100, 'B':200}

p1 = { key:value for key, value in prices.items() if value > 200 }

tech_name = {'A', 'C', 'D'}
p2 = { key:value for key, value in prices.items() if key in tech_name }

# 튜플 시퀀스를 만들고 dict() 함수에 전달 - 속도가 나쁘다
# dictionary comprehension을 사용하는 것이 효과적이다.
p1 = dict((key, value) for key, value in prices.items() if value > 200)

p2 = { key:prices[key] for key in prices.keys() & tech_name }
