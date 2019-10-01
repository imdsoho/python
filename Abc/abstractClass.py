from abc import ABCMeta, abstractmethod

class TupleABC(metaclass=ABCMeta):
    @abstractmethod
    def abcFunc(self):
        pass

class MyTuple(TupleABC):
    def abcFunc(self):
        pass

    def myTupleCustomFunc(self):
        print ("myTupleCustomFunc")
        return ('a', 'b')

TupleABC.register(tuple)

assert issubclass(tuple, TupleABC)
assert isinstance((), TupleABC)

mt = MyTuple()
tup_data = (1,2,3)

#ret_tuple = mt.myTupleCustomFunc()
#print(ret_tuple)