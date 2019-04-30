#-*- coding: utf-8 -*-

# 연산객체 - 첫번째 숫자, 연산자, 두번째 숫자, 연산객체(??) 가 만든 결과값으로 연산결과 출력값을 생성
from abc import abstractmethod, ABCMeta

#class AbstractOperation(metaclass=ABCMeta):
class AbstractOperation():
    __metaclass__ = ABCMeta

    def __init__(self):
        self.firstNumber = 0
        self.secondNumber = 0

    def operate(self):
        firstNumber = self.getFirstNumber()
        secondNumber = self.getSecondNumber()

        operator = self.getOperator()

        operatorDescription = operator.getDescription()

        answer = operator.getAnswer(firstNumber, secondNumber)

        result = str(firstNumber) + operatorDescription + str(secondNumber) + " = " + str(answer)

        self.__print(result)

    @abstractmethod
    def getOperator(self):
        pass

    def getFirstNumber(self):
        return self.firstNumber

    def setFirstNumber(self, firstNumber):
        self.firstNumber = firstNumber

    def getSecondNumber(self):
        return self.secondNumber

    def setSecondNumber(self, secondNumber):
        self.secondNumber = secondNumber

    def __print(self, result):
        print(result)
