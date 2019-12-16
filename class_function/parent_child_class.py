class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data):
        return False

class UnknownEvent(Event):
    pass

class LoginEvent(Event):
    def __init__(self, event_data):
        print("LOGIN instance")

    @staticmethod
    def meets_condition(event_data):
        return True

class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data):
        return False

class SystemMonitor:
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        print(Event.__subclasses__())
        print(len(Event.__subclasses__()))

        for event_cls in Event.__subclasses__():
            print(event_cls)
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue

        return UnknownEvent(self.event_data)

event_data_dict = {}
monitor = SystemMonitor(event_data_dict)
monitor.identify_event()
