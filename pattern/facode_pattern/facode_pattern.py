class EventManager(object):
    def __init__(self):
        print("Event Manager")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()

class Hotelier(object):
    def __init__(self):
        print("Arrange Hotel")

    def __isAvailable(self):
        print("__isAvailable")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking")

class Florist(object):
    def __init__(self):
        print("Flower Decoration")

    def setFlowerRequirements(self):
        print("Carnation, Rose and Lilies")

class Caterer(object):
    def __init__(self):
        print("Food Arrangement")

    def setCuisine(self):
        print("Chinese & Contiental Cuisine")

class Musician(object):
    def __init__(self):
        print("Musical Arrangements")

    def setMusicType(self):
        print("Jazz and Classical")

class You(object):
    def __init__(self):
        print("You:: Whoa!")

    def askEventManager(self):
        print("You:: Let's Contact the Event Manager")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You:: Thanks to Event Maanger")


you = You()
you.askEventManager()


