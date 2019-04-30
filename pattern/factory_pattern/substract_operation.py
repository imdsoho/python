
from abstract_operation import AbstractOperation
from substract_operator import SubstractOperator

class SubstractOperation(AbstractOperation):
    
    def getOperator(self):
        return SubstractOperator()
