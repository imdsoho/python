#-*- coding: utf-8 -*-

from abstract_operation import AbstractOperation

class SubstractOperation(AbstractOperation):
 
    def getAnswer(self, firstNumber, secondNumber):
        return firstNumber - secondNumber
    
    def getOperator(self):
        return "-"
