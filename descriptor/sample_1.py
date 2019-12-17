class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        print("__get__(%s, %r, %r)" % (self.__class__.__name__, instance, owner))
        #print(type(instance))
        #print(instance.__class__.__name__)
        #print(owner.__name__)

        return instance

    def __str__(self):
        return "DescriptorClass instance"

class ClientClass:
    descriptor = DescriptorClass()

class UserClass:
    pass

client = ClientClass()
print(client.descriptor)

print("---------------")

user = UserClass()
user.descriptor = DescriptorClass()
print(user.descriptor)

#descriptor = DescriptorClass()
#print(descriptor)

class Attribute:
    value = 42

    def __str__(self):
        return "Attribute intance"

class Client:
    attribute = Attribute()

#instance = Client()
#print(instance.attribute)
#print(instance.attribute.value)
