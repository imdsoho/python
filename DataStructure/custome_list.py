class FrequencyList(list):
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        counts = {}

        #print("0 : ", dir(super))
        #print("1 : ", type(self))
        #print("2 : ", self)
        print("3 : ", dir(self))

        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1

        return counts

foo = FrequencyList(['a', 'b', 'c', 'd', 'a', 'b'])

#print("Length is ", len(foo))
#foo.pop()
#print('After pop : ', repr(foo))

#print(foo.frequency())
#print(FrequencyList.mro())

list_info = []
print(dir(list_info))