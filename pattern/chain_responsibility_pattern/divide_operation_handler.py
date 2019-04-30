
from abstract_operation_handler import AbstractOperationHandler

class DivideOperationHandler(AbstractOperationHandler):
    
    def __init__(self, operator):
        AbstractOperationHandler.__init__(self, operator)
    
    def operate(self, request):
        operator = self.getOperator()

        firstNumber = request.getFirstNumber(operator)
        secondNumber = request.getSecondNumber(operator)

        return firstNumber / secondNumber
