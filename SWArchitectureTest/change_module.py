class RuntimeChangeDataModule():
    def get_data(self):
        ret_data = {}
        ret_data["A"] = "2"
        return ret_data

def get_class():
    cls = RuntimeChangeDataModule()

    return cls
