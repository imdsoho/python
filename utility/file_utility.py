# 튜플을 CSV 파일로 출력
s = ('ACME', 50, 123.45)
print (','.join(str(x) for x in s))

# 디렉토리에 .py 파일이 있는지 확인
import os
files = os.listdir('dir_path_name')
if any(name.endswith('.py') for name in files):
    print ('There is python')
else:
    print ('No python')
