# zip() 은 단 한 번만 소비할 수 있는 iterator를 생성한다. 동일한 갯수의 요소값을 갖는 시퀀스 자료형을 묶어주는 역할

zip([1,2,3], ['a','b'])
# [(1, 'a'), (2, 'b')]

zip([1,2,3], ['a','b','c'])
# [(1, 'a'), (2, 'b'), (3, 'c')]

prices = { 'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

min(prices, key=lambda k: prices[k])

max(prices, key=lambda k: prices[k])

min_value = prices[min(prices, key=lambda k: prices[k])]

min(zip(prices.values(), prices.keys()))
# (10.75, 'FB')

max(zip(prices.values(), prices.keys()))
# (612.78, 'AAPL')