class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value:str):
        if not isinstance(value, str):
            raise TypeError('expected a string')

        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")

if __name__ == "__main__":
    a = Person("Guido")
    print(a.first_name)

    #a.first_name = 42
    #a.first_name = "Guido2"
    #del a.first_name
    #print(a.first_name)

    #print(a.__dict__)
    print(Person.__dict__)
    print(Person.first_name)







