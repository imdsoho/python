from weakref import WeakKeyDictionary

class DescriptorClass:
    def __init__(self, init_value):
        self.value = init_value
        self.mapping = WeakKeyDictionary()

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return self.mapping.get(instance, self.value)

    def __set__(self, instance, value):
        self.mapping[instance] = value

