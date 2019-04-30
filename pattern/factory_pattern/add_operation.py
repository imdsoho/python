#-*- coding: utf-8 -*-

from abstract_operation import AbstractOperation
from add_operator import AddOperator

class AddOperation(AbstractOperation):
    def getOperator(self):
        return AddOperator()
