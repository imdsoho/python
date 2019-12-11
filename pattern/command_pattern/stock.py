from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()

class StockTrade:
    def buy(self):
        print("Buy Stock")

    def sell(self):
        print("Sell Stock")

class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

if __name__ == "__main__":
    stock = StockTrade()

    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
