#-*- coding: utf-8 -*-

from add_operation import AddOperation
from substract_operation import SubstractOperation
from multiply_operation import MultiplyOperation
from divide_operation import DivideOperation

# 템플릿 패턴
# 상속을 통해 슈퍼클래스의 기능을 확장할 때 사용하는 가장 대표적인 방법이다.
# 변하지 않는 기능은 슈퍼클래스에 만들어 두고
# 자주 변경되며 확장할 기능은 추상클래스나 오버라이딩 가능한 protected메소드(=추상메소드) 등으로 만든 뒤 서브클래스에서 만들도록 한다.
# -단점 : 상속을 통하여 구현이 되므로 해당 추상 메소드가 필요한 클래스마다 상속을 받아야 한다.

class Client:
   
    def main(self):
        firstNumber = 100
        secondNumber = 20

        operations = (AddOperation(),
                SubstractOperation(), MultiplyOperation(),
                 DivideOperation())

        for operation in operations:
            operation.setFirstNumber(firstNumber)
            operation.setSecondNumber(secondNumber)

            operation.operate()
         
client = Client()
client.main()