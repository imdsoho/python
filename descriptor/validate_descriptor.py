class Validation:
    def __init__(self, validation_function, error_msg:str):
        self.validation_function = validation_function
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_function(value):
            raise ValueError(f"{value!r} {self.error_msg}")

class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__[self._name]

    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value

class ClientClass:
    descriptor1 = Field(
        Validation(lambda x: isinstance(x, (int, float)), "is not number")
    )

    descriptor2 = Field(
        Validation(lambda x: x >= 0, "is smaller than 0")
    )

client = ClientClass()

client.descriptor1 = 50
client.descriptor2 = 51

print(client.__dict__)
