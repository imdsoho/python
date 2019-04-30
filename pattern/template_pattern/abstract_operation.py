#-*- coding: utf-8 -*-


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

        answer = self.getAnswer(firstNumber, secondNumber)

        result = str(firstNumber) + operator + str(secondNumber) + " = " + str(answer)

        self.printResult(result)

    @abstractmethod
    def getOperator(self):
        pass

    @abstractmethod
    def getAnswer(self, firstNumber, secondNumber):
        pass

    def printResult(self, result):
        print(result)

    def getFirstNumber(self):
        return self.firstNumber

    def setFirstNumber(self, firstNumber):
        self.firstNumber = firstNumber

    def getSecondNumber(self):
        return self.secondNumber

    def setSecondNumber(self, secondNumber):
        self.secondNumber = secondNumber
