
from abc import abstractmethod, ABCMeta

class AbstractOperationHandler(metaclass=ABCMeta):
    
    def __init__(self, operator):
        self.operator = operator
        self.next = None
        
    def setNext(self, _next):
        self.next = _next
        return self.next

    def handleRequest(self, request):
        if self.resolve(request):
            result = self.operate(request)
            return result
        elif self.next != None:
            return self.next.handleRequest(request)
        else:
            self.handleFail(request)
            return 0

    def handleFail(self, request):
        print("fail")

    def getOperator(self):
        return self.operator

    @abstractmethod
    def operate(self, request):
        pass

    def resolve(self, request):
        if request.getExpression().find(self.getOperator()) >= 0:
            return True

        return False   
