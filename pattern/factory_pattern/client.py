#-*- coding: utf-8 -*-

from add_operation import AddOperation
from substract_operation import SubstractOperation
#from multiply_operation import MultiplyOperation
#from divide_operation import DivideOperation

# 팩토리 패턴
# 템플릿 메소드와 마찬가지로 상속을 통해 기능을 확장하게 하는 패턴이다.

# 이 패턴의 주체는 서브클래스로 생각하면 되것다.
# 서브클래스에서 오브젝트 생성 방법과 클래스를 결정할 수 있도록 미리 정의해둔 메소드를 팩토리 메소드라 하고

# 이 방식을 통해 오브젝트 생성방법을 나머지 로직, 즉 슈퍼클래스의 기본 코드에서 독립시키는 방법을
# 팩토리 메소드 패턴이라 한다. 이 메소드는 주로 인터페이스 타입으로 오브젝트를 리턴한다.
# 자바에서 종종 오브젝트를 생성하는 기능을 가진 메소드를 일반적으로 팩토리 메소드라고
# 부르기도 하는데 이때 말하는 팩토리 메소드와는 다르다고 한다.

class Client:
    def main(self):
        firstNumber = 100
        secondNumber = 20

        #operations = (AddOperation(), SubstractOperation(), MultiplyOperation(), DivideOperation())
        operations = (AddOperation(), SubstractOperation())

        for operation in operations:
            operation.setFirstNumber(firstNumber)
            operation.setSecondNumber(secondNumber)

            operation.operate()

client = Client()
client.main()
