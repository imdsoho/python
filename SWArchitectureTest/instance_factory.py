from dataService import DataObjectService

def getInstance(clsName):
    instance = clsName()

    if isinstance(instance, DataObjectService):
        print("TRUE")
    else:
        print("FALSE")
        instance = None

    return instance
