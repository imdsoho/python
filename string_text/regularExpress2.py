import re

# 여러 줄에 걸친 정규표현식 사용
comment = re.compile(r'/\*(.*?)\*/')
text = '''/* This is a 
multiline comment */
'''

comment_multiline = re.compile(r'/\*((?:.|\n)*?)\*/')
comm = comment_multiline.findall(text)
print(comm)

# 정규표현식의 점(.)에 개행문을 포함한 모든 문자 매칭
# 복잡한 패턴 등에서 문제가 발생할 수 있다.
comment_dotall = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comm = comment_dotall.findall(text)
print(comm)

