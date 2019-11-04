# Python 3.6
logest_tokens = ['a','b','c','d', 'e', 'f', 'g']

nexts = logest_tokens[1:]
nexts.append(None)

for logest_token, n in list(zip(logest_tokens, nexts)):
#for logest_token, n in zip(logest_tokens, nexts):
#from itertools import izip
#for logest_token, next in izip(logest_tokens, nexts):
    print(logest_token, ":", n)

'''zip36 = zip(range(5), range(5))
print(type(zip36))
print(next(zip36))
print(help(zip))'''


"""
Python 2.7 - itertools 사용

from itertools import izip

logest_tokens = ['a','b','c','d', 'e', 'f', 'g']

nexts = logest_tokens[1:]
nexts.append(None)

for logest_token, n in izip(logest_tokens, nexts):
    print logest_token, ":", n
"""