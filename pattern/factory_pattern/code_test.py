from abc import ABCMeta, abstractmethod

class Connector(object):
    """A client."""
    def __init__(self, factory):
        """factory is a AbstractFactory instance which creates all attributes of a connector according to factory class."""
        self.protocol = factory.create_protocol()
        self.port = factory.create_port()
        self.parse = factory.create_parser()

    def read(self, host, path):
        url = self.protocol + '://' + host + ':' + str(self.port) + path
        print('Connecting to ', url)
        return 'factory is a AbstractFactory instance which creates all attributes of a connector according to factory class.'

    @abstractmethod
    def parse(self):
        pass

class Factory():
    def create_protocol(self):
        return "http"

    def create_port(self):
        return '80'

    def create_parser(self):
        return 'content - filenames array'

if __name__ == '__main__':
    domain = 'ftp.freebsd.org'
    path = '/pub/FreeBSD/'

    factory = Factory()
    connector = Connector(factory)

    try:
        content = connector.read(domain, path)
    except Error as e:
        print('Can not access resource with this method')
    else:
        print(connector.parse(content))
