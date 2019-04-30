
class Request:
    
    def __init__(self, expression):
        self.expression = expression
    
    def getExpression(self):
        return self.expression

    def getFirstNumber(self, operator):
        operatorIndex = self.expression.index(operator)
        
        firstNumber = self.expression[0:operatorIndex]
        return int(firstNumber)

    def getSecondNumber(self, operator):
        operatorIndex = self.expression.index(operator)
        
        secondNumber = self.expression[operatorIndex + 1]
        return int(secondNumber)
