class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called.")
        else:
            #print("instance already created: ", self.getInstance())
            print("instance already created")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()

        return cls.__instance

s = Singleton.getInstance()
print("[S]: ", id(s))
s1 = Singleton.getInstance()
print("[S1]: ", id(s1))
