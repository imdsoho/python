
global_vo_data = "None"

class SampleVO:
    class_vo_data = "None"

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.instance_dict_data = {key : value}

    def set_key(self, data):
        self.key = data
    def get_key(self):
        return self.key

    def set_value(self, data):
        self.value = data
    def get_value(self):
        return self.value

    def get_dict(self):
        return self.instance_dict_data

    def __str__(self):
        return str(self.key) + " : " + str(self.value) + " : " + str(self.instance_dict_data)

    def modify_data(self):
        self.instance_dict_data = {"key_change" : "value_change"}

    def set_global_var(self, data):
        global global_vo_data
        global_vo_data = data

    def get_global_var(self):
        global global_vo_data
        return global_vo_data

    def set_class_var(self, data):
        SampleVO.class_vo_data = data

    def get_class_var(self):
        return SampleVO.class_vo_data
