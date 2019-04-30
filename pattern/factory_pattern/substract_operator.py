
from abstract_operator import AbstractOperator

class SubstractOperator(AbstractOperator):
    
    def getAnswer(self, firstNumber, secondNumber):
        return firstNumber - secondNumber

    def getDescription(self):
        return "-"
