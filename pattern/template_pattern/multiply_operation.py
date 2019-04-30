#-*- coding: utf-8 -*-

from abstract_operation import AbstractOperation

class MultiplyOperation(AbstractOperation):
 
    def getAnswer(self, firstNumber, secondNumber):
        return firstNumber * secondNumber
    
    def getOperator(self):
        return "*"
