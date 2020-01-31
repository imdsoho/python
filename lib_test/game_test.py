#import game.sound.echo
#print(game.sound.echo.echo_test())

#from game.sound import echo
#print(echo.echo_test())

#from game.sound.echo import echo_test
#print(echo_test())

#import game
'''
game 디렉토리의 모듈 또는 game 디렉토리의 __init__.py에 정의한 것만을 참조
'''
#print(game.sound.echo.echo_test())  # ERROR

#import game.sound.echo.echo_test    # ERROR
'''
dot(.) 연산자를 사용해서 import a.b.c 처럼 import 할 때
가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
'''
#print(echo_test())


'''
__init__.py 파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할
'''
#from game.sound import *
#print(echo.echo_test()) # ERROR
'''
특정 디렉토리의 모듈을 *를 사용하여 import 할 때는
해당 디렉토리의 __init__.py 파일에 
__all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야 한다.
'''
'''
/game/sound/__init__.py
__all__ = ['echo']
'''
from game.sound import *
print(echo.echo_test())

'''
__all__이 의미하는 것은 sound 디렉토리에서 * 기호를 사용하여
import 할 경우 이곳에 정의된 echo 모듈만 import 된다.
'''
#print(echo_change.echo_change())   # ERROR

'''
from a.b.c import * 에서 from의 마지막 항목인 c 가 모듈인 경우,
__all__과 상관없이 무조건 import 된다.
'''



