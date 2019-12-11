from abc import ABCMeta, abstractmethod

class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    @abstractmethod
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()

class VeniceTrip(Trip):
    def setTransport(self):
        print("Venice Transport")

    def day1(self):
        print("Venice day-1")

    def day2(self):
        print("Venice day-2")

    def day3(self):
        print("Venice day-3")

    def returnHome(self):
        print("Venice return Home")

class MaldivesTrip(Trip):
    def setTransport(self):
        print("Maldives Transport")

    def day1(self):
        print("Maldives day-1")

    def day2(self):
        print("Maldives day-2")

    def day3(self):
        print("Maldives day-3")

    def returnHome(self):
        print("Maldives return Home")

class TravelAgency:
    def arrange_trip(self):
        choice = "1"

        if choice == "1":
            self.trip = VeniceTrip()
            self.trip.itinerary()

        if choice == "2":
            self.trip = MaldivesTrip()
            self.trip.itinerary()

TravelAgency().arrange_trip()

