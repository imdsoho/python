
from com.bsb.calc.chain.add_operation_handler import AddOperationHandler
from com.bsb.calc.chain.substract_operation_handler import SubstractOperationHandler
from com.bsb.calc.chain.multiply_operation_handler import MultiplyOperationHandler
from com.bsb.calc.chain.divide_operation_handler import DivideOperationHandler
from com.bsb.calc.chain.request import Request

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
