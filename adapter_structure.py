import abc

class Target(metaclass=abc.ABCMeta):
    """Defines the domain-specific interface that Client uses."""
    def __init__(self):
        super(Target, self).__init__()

    @abc.abstractmethod
    def request(self):
        pass


class Client(object):
    """Collaborates with objects conforming to the Target interface."""
    def __init__(self, target):
        super(Client, self).__init__()
        self.target = target
        # ...
        target.request()


class Adaptee(object):
    """Defines an existing interface that needs adapting"""
    def __init__(self):
        super(Adaptee, self).__init__()
    
    def existingRequest(self):
        # Do something useful


class Adapter(Target, Adaptee):
    """
    Adapts the interface of Adaptee to the Target interface.
    This is the class version of the Adapter pattern. The object version will
    compose an instance of Adaptee, instead of subclassing from it.
    """
    def __init__(self):
        super(Adapter, self).__init__()
        
    def request(self):
        # Might need to do some set up here
        self.existingRequest()
        # Might need to do some teardown here