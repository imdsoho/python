import weakref
import sys

class ObjectManager:
    def __init__(self):
        self.weakDict = weakref.WeakValueDictionary()
        self.strongDict = dict()

    def InputObject(self, obj):
        objectID = id(obj)
        print(objectID)         # 2430464260864
        self.weakDict[objectID] = obj
        self.strongDict[objectID] = obj
        return objectID

    def GetObject(self, objectID):
        try:
            return self.weakDict[objectID]
        except:
            return None


class Apple:
    pass

red_apple = Apple()
print(sys.getrefcount(red_apple))   # 2

red_apple.color = 'red'
print(sys.getrefcount(red_apple))   # 2

object_manager = ObjectManager()
red_id = object_manager.InputObject(red_apple)

print(sys.getrefcount(red_apple))   # 3

#print(red_apple.color)
#print(object_manager.GetObject(red_id).color)

#print(red_apple is object_manager.GetObject(red_id))
#print(id(red_apple))
#print(id(object_manager.GetObject(red_id)))

del red_apple

''' 
self.strongDict[objectID] = obj
obj(= red_apple)을 value 값으로 넣으면
del red_apple을 해도 객체가 살아있음
'''
print(id(object_manager.GetObject(red_id))) # 2430464260864

print(sys.getrefcount(object_manager.GetObject(red_id))) # refcount = 2
print(sys.getrefcount(red_apple))   # Error - del red_apple