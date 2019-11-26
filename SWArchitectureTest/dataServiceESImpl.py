from dataService import DataObjectService

class DataObjectESServiceImpl(DataObjectService):
    def __init__(self):
        pass

    def get_data(self):
        data_dict = {"type": "ES", "id": "1", "value": "001"}

        return data_dict
