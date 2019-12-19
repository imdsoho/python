class HistoryTracedAttribute:
    def __init__(self, trace_attribute_name):
        print("-1-")
        self.trace_attribute_name = trace_attribute_name
        self._name = None

    def __set_name__(self, owner, name):
        print("-2- > ", name)
        self._name = name

    def __get__(self, instance, owner):
        print("-3-")
        if instance is None:
            return self

        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        print("-4-")
        self._track_change_in_value_for_instance(instance, value)
        instance.__dict__[self._name] = value

    def _track_change_in_value_for_instance(self, instance, value):
        print("-5-")
        self._set_default(instance)

        if self._needs_to_track_change(instance, value):
            instance.__dict__[self.trace_attribute_name].append(value)

    def _needs_to_track_change(self, instance, value):
        print("-6-")
        try:
            current_value = instance.__dict__[self._name]
        except KeyError:
            return True

        return value != current_value

    def _set_default(self, instance):
        print("-7-")
        instance.__dict__.setdefault(self.trace_attribute_name, [])

class Traveller:
    current_city = HistoryTracedAttribute("cities_visited")

    def __init__(self, name, current_city):
        self.name = name
        self.current_city = current_city


traveller = Traveller("jsc", "seoul")
print("------------------")
traveller.current_city = "busan"
print("------------------")
print(traveller.cities_visited)
