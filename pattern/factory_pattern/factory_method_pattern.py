from abc import ABCMeta, abstractmethod

class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("Personal Section")

class AlbumSection(Section):
    def describe(self):
        print("Album Section")

class PatentSection(Section):
    def describe(self):
        print("Patent Section")

class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.section = []
        self.createProfile()

    @abstractmethod
    def createProfile(self):
        pass

    def getSection(self):
        return self.section

    def addSection(self, section):
        self.section.append(section)

class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())

if __name__ == "__main__":
    profile_type = "linkedin"

    profile = eval(profile_type.lower())()
    print("create profile..", type(profile).__name__)
    print("Profile has sections - ", profile.getSection())

