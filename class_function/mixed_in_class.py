class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)


class InspectClass():
    def __init__(self):
        self.name = "jsc"
        self.id = "1"

    def to_dict(self):
        data_dict = {}
        return data_dict

    def show_dict(self):
        print(self.__dict__)

cls = InspectClass()
cls.show_dict()