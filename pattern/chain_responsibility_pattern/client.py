
from add_operation_handler import AddOperationHandler
from substract_operation_handler import SubstractOperationHandler
from multiply_operation_handler import MultiplyOperationHandler
from divide_operation_handler import DivideOperationHandler
from request import Request

class Client:
   
    def main(self):
        addOperationHandler = AddOperationHandler("+")
        substractOperationHandler = SubstractOperationHandler("-")
        multiplyOperationHandler = MultiplyOperationHandler("*")
        divideOperationHandler = DivideOperationHandler("/")
        
        addOperationHandler.setNext(substractOperationHandler).setNext(multiplyOperationHandler).setNext(divideOperationHandler)

        requests = [Request("100+20"), Request("100-20"), Request("100*20"), Request("100/20")]
        
        for request in requests:
            answer = addOperationHandler.handleRequest(request)
            expression = request.getExpression()
            
            print(expression," = ",answer)
        
client = Client()
client.main()
