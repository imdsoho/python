class NonDataDescriptor:
    def __get__(self, instance, owner):
        if instance is None:
            return self

        return 42

class ClientClass:
    descriptor = NonDataDescriptor()

client = ClientClass()
print(client.descriptor)

print(vars(client))
#print(client.__dict__)

client.descriptor = 99
print(vars(client))
print(client.descriptor)
