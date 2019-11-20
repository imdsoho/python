class ValidatingDB(object):
    def __init__(self):
        self.exists = 5

    # ValidatingDB 클래스에서 오버라이딩
    def __getattr__(self, name):
        print('Called __getattr__(%s)' % name)
        value = '...'
        setattr(self, name, value)

        return value

    # ValidatingDB 클래스에서 오버라이딩
    def __getattribute__(self, name):
        print('Called __getattribute__(%s)' % name)

        try:
            return super().__getattribute__(name)
        except AttributeError as err:
            #value = 'default'
            #setattr(self, name, value)
            #return value

            self.__getattr__(name)

data = ValidatingDB()
print(data.exists)
print("-----------------")
print(data.foo)
print("-----------------")
print(data.foo)

