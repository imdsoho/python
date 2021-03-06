# 라이브러리(library)란 특정한 기능을 구현하기 위해 미리 작성된 프로그램
# 파이썬 라이브러리는 모듈과 패키지로 나눈다.

# 모듈(module)은 함수나 클래스 등의 객체 정의를 포함하는 파일 하나를 가리킨다.
# 모듈에는 실행문을 작성할 수 있다. 실행문은 보통 해당 모듈을 초기화하기 위한 것으로
# 이 모듈을 어디선가 처음 읽어들였을 때 단 한번 실행된다.

# 패키지(package)는 여러 개의 모듈을 하나로 묶어 관리하는 것이다.
# 패키지는 모듈 파일이 여러 개 포함된 디렉토리이다.
# 패키지 안의 폴더에는 __init__.py라는 파일이 있다.
# 패키지를 import하면 우선 이 파일을 읽어들인다.
# 이 파일에는 패키지를 import할 때 실행하고 싶은 처리를 작성해둔다.

# 모듈을 import할 때 진행되는 내용은 다음과 같다.
# 1. 새로운 네임스페이스를 만들고 import하는 모듈 안의 객체를 모두 이곳에 저장한다.
# 2. import하는 모듈 안의 코드를 새 네임스페이스 안에서 실행한다.
# 3. 모듈이 import한 네임스페이스에 새로 만든 네임스페이스에 대한 참조명을 만든다.
# 이 참조명은 모듈의 이름과 같다.

# import 방법
# 1. import 모듈명
# 2. import 모듈명 as 별명
# 3. from 모듈명 import 모듈요소명1, 모듈요소명2(함수, 클래스, 변수 등)
# 4. from 모듈명 import * (PEP 8에서 권장하지 않음)
# 5. from 모듈명 import 모듈요소명 as 별명
# 6. import 모듈명1, 모듈명2

# package import 방법
# 1. import 패키지명
# 2. from 패키지명 import 패키지명1, 패키지명2
# 3. from 패키지명 import *
# 4. import 패키지명 as 별명
# 5. from 패키지명 import 모듈명 as 별명
# 6. import 패키지명.모듈명
# 7. import 패키지명.모듈명 as 별명
# 8. import 패키지명1, 패키지명2

# 파일을 검색하는 순서
# 파이썬에서 모듈을 import할 때 import하려는 이름의 모듈이 여러 군데 존재하는 경우
# 미리 정해진 우선순위에 따라 모듈을 검색해서 가장 처음 발견된 모듈을 import 한다.
# 1. 현재 작업 디렉토리
# 2. 환경변수 PYTHONPATH에 설정된 디렉토리
# 3. 표준 라이브러리의 모듈 디렉토리
# 4. 서드파티 라이브러리의 모듈 디렉토리

import sys
libarr = sys.path
for path in libarr:
    print(path)

# [참조][책] 엔지니어를 위한 파이썬