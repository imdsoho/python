#-*- coding: utf-8 -*-

from abstract_operator import AbstractOperator

class AddOperator(AbstractOperator):
    def getAnswer(self, firstNumber, secondNumber):
        return firstNumber + secondNumber

    def getDescription(self):
        return "+"

