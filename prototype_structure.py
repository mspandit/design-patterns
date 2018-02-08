import abc


class Client(object):
    """Creates a new object by asking a prototype to clone itself."""
    def __init__(self, prototype):
        super(Client, self).__init__()
        self.prototype = prototype
    
    def operation(self):
        p = self.prototype.clone()
        # do something to p
        return p


class Prototype(metaclass=abc.ABCMeta):
    """Declares an interface for cloning itself."""
    def __init__(self):
        super(Prototype, self).__init__()
        
    @abc.abstractmethod
    def clone(self):
        pass
        

class ConcretePrototype1(Prototype):
    """Implements an operation for cloning itself."""
    def __init__(self):
        super(ConcretePrototype1, self).__init__()
    
    def clone(self):
        return # copy of self


class ConcretePrototype2(Prototype):
    """Implements an operation for cloning itself."""
    def __init__(self):
        super(ConcretePrototype2, self).__init__()

    def clone(self):
        return # copy of self