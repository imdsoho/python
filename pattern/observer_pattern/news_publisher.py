from abc import ABCMeta, abstractmethod

class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return "Got News: ", self.__latestNews

class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass

class SMSSubscriber:
    def __init__(self, publiser):
        self.publisher = publiser
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class EmailSubscriber:
    def __init__(self, publiser):
        self.publisher = publiser
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

class AnyOtherSubscriber:
    def __init__(self, publiser):
        self.publisher = publiser
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())

if __name__ == "__main__":
    news_publisher = NewsPublisher()

    for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscriber(news_publisher)
    print("Subscribers: ", news_publisher.subscribers())

    news_publisher.addNews("Hello World!!")
    news_publisher.notifySubscribers()

    print("Detach: ", type(news_publisher.detach()).__name__)
    news_publisher.notifySubscribers()

    news_publisher.addNews("My Second News")
    news_publisher.notifySubscribers()
