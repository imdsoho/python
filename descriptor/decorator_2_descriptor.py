"""Clean Code in Python - Chapter 6: Descriptors

> Using descriptors instead of class decorators

"""
from datetime import datetime
from functools import partial
from typing import Any, Callable


class BaseFieldTransformation:
    """Base class to define descriptors that convert values."""

    def __init__(self, transformation: Callable[[Any, str], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self
        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value

#base = BaseFieldTransformation(lambda x: x)
#print("[0]", type(base))

ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(
    BaseFieldTransformation, transformation=lambda x: "**redacted**"
)
FormatTime = partial(
    BaseFieldTransformation,
    transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"),
)

print("[1]", type(ShowOriginal))
print("[1-1]", ShowOriginal)

class LoginEvent:
    username = ShowOriginal()
    password = HideField()
    ip = ShowOriginal()
    timestamp = FormatTime()

    #print("[2]", type(username))

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

        #print("[3]", type(username))

    def serialize(self):
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }


class BaseEvent:
    """Abstract the serialization and the __init__"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def serialize(self):
        return {
            attr: getattr(self, attr)
            for attr in self._fields_to_serialize()
        }

    def _fields_to_serialize(self):
        for attr_name, value in vars(self.__class__).items():
            if isinstance(value, BaseFieldTransformation):
                yield attr_name


class NewLoginEvent(BaseEvent):
    """A class that takes advantage of the base to only define the fields."""

    username = ShowOriginal()
    password = HideField()
    ip = ShowOriginal()
    timestamp = FormatTime()


le = LoginEvent("usr", "1234567890", "127.0.0.1", datetime(2016, 7, 20, 15, 45))
#print(vars(le))
print(le.serialize())
#print(le.password)
print("---------------------")

le_2 = NewLoginEvent(username="usr-2", password="abcdefg", ip="127.0.0.1", timestamp=datetime(2016, 7, 20, 15, 45))
print(le_2.serialize())
print("---------------------")

le_2.username = "AAAAAAAAAAAAA"
#print(le.serialize())
#print(le_2.serialize())
#print(vars(le))
#print(vars(le_2))