#-*- coding: utf-8 -*-

# 연산자 객체 - 결과값을 만든다.
from abc import abstractmethod, ABCMeta

#class AbstractOperator(metaclass=ABCMeta):
class AbstractOperator():
    __metaclass__ = ABCMeta

    @abstractmethod
    def getAnswer(self, firstNumber, secondNumber):
        pass

    @abstractmethod
    def getDescription(self):
        pass

