class DataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        return 42

    def __set__(self, instance, value):
        print("%s.descriptor = %s", instance, value)
        instance.__dict__["descriptor"] = value

class ClientClass:
    descriptor = DataDescriptor()

client = ClientClass()
print(vars(client))

client.descriptor = 99
print(vars(client))
print(client.descriptor)
print(client.__dict__["descriptor"])

