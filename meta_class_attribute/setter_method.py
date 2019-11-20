class Registor(object):
    def __init__(self, ohms):
        #print("-1-")
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

class VoltageResistance(Registor):
    def __init__(self, ohms):
        #print("-2-")
        super().__init__(ohms)
        #print("-3-")
        self._voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage /self.ohms

    @property
    def ohms(self):
        return self._ohms

    '''@ohms.setter
    def ohms(self, ohms):
        #print("-4-")
        if ohms <= 0:
            raise  ValueError('%f ohms must be > 0' % ohms)

        self._ohms = ohms'''

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")

        self._ohms = ohms


#r2 = VoltageResistance(1e3)
#print('Before: %5r amps' % r2.current)

#r2.voltage = 10
#print('After: %5r amps' % r2.current)

r3 = VoltageResistance(-5)
#r3.ohms = 100      # raise AttributeError("Can't set attribute")

