# 유니코드 텍스트 normalize
import unicodedata
s1 = 'Spicy Jalapeno'
s2 = 'Spicy Jalapeno'

t1 = unicodedata.normalize('NFC', s1)
print(t1)

t3 = unicodedata.normalize('NFD', s1)
print(t3)