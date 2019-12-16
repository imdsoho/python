class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False

    @staticmethod
    def meets_condition_pre(event_data: dict):
        """Precondition of the contract of this interface.

        Validate that the ``event_data`` parameter is properly formed.
        """
        assert isinstance(event_data, dict), f"{event_data!r} is not a dict"

        for moment in ("before", "after"):
            assert moment in event_data, f"{moment} not in {event_data}"
            assert isinstance(event_data[moment], dict)


class UnknownEvent(Event):
    """A type of event that cannot be identified from its data"""


class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"].get("session") == 0 and event_data["after"].get("session") == 1
        )


class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return (
            event_data["before"].get("session") == 1 and event_data["after"].get("session") == 0
        )


class TransactionEvent(Event):
    """Represents a transaction that has just occurred on the system."""

    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["after"].get("transaction") is not None


class SystemMonitor:
    """Identify events that occurred in the system
    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        Event.meets_condition_pre(self.event_data)

        event_cls = next(
            #iterator
            (
                # 제너레이터
                event_cls
                for event_cls in Event.__subclasses__()
                if event_cls.meets_condition(self.event_data)
            ),
            # default
            UnknownEvent,
        )
        return event_cls(self.event_data)


l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
print(l1.identify_event().__class__.__name__)
#'LoginEvent'

#l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
#l2.identify_event().__class__.__name__
#'LogoutEvent'

#l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
#l3.identify_event().__class__.__name__
#'UnknownEvent'

#l4 = SystemMonitor({"before": {}, "after": {"transaction": "Tx001"}})
#l4.identify_event().__class__.__name__
#'TransactionEvent'