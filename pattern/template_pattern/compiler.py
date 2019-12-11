from abc import ABCMeta, abstractmethod

class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()

class iOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Source Code")

    def compileToObject(self):
        print("Compile code to Object")

    def run(self):
        print("Program Run")

iOS = iOSCompiler()
iOS.compileAndRun()
