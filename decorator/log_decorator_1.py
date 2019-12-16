import unittest
from datetime import datetime

def hide_field(field) -> str:
    return "**redacted**"

def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")

def show_original(event_field):
    return event_field

class EventSerializer:
    def __init__(self, serialization_fields: dict) -> None:
        print("-2-")
        self.serialization_fields = serialization_fields

    def serialize(self, event) -> dict:
        print("-5-")
        return {
            field: transformation(getattr(event, field))

            for field, transformation in self.serialization_fields.items()
        }

class Serialization:
    def __init__(self, **transformations):
        print("-1-")
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        print("event_class : ", event_class.__name__)  # LoginEvent
        def serialize_method(event_instance):
            print("-4-")
            return self.serializer.serialize(event_instance)

        event_class.serialize = serialize_method
        print("-3-")
        return event_class

@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time,
)
class LoginEvent:
    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

if __name__ == "__main__":
    event = LoginEvent(
        "UserName", "password", "127.0.0.1", datetime(2016, 7, 20, 15, 45)
    )
    print(event.serialize())