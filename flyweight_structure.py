import abc


class Flyweight(metaclass=abc.ABCMeta):
    """ 
    Declares an interface through which flyweights can receive and act on 
    extrinsic state.
    """
    def __init__(self):
        super(Flyweight, self).__init__()

    @abc.abstractmethod
    def operation(extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Implements the Flyweight interface and adds storage for intrinsic state, if
    any. A ConcreteFlyweight object must be shareable. Any state it stores must
    be intrinsic; that is, it must be independent of the ConcreteFlyweight
    object's context.
    """
    def __init__(self, intrinsicState):
        super(ConcreteFlyweight, self).__init__()
        self.intrinsicState = intrinsicState
    
    def operation(extrinsic_state):
        # extrinsic_state must include any required (unshared) context
        

class UnsharedConcreteFlyweight(Flyweight):
    """
    Not all Flyweight subclasses need to be shared. The Flyweight interface
    *enables* sharing; it doesn't enforce it. It's common for 
    UnsharedConcreteFlyweight objects to have ConcreteFlyweight objects as
    children at some level in the flyweight object structure.
    """
    def __init__(self):
        super(UnsharedConcreteFlyweight, self).__init__()

    def operation(extrinsic_state):
        # extrinsic_state must include any required (unshared) context


class FlyweightFactory(object):
    """
    Creates and manages flyweight objects.
    Ensures that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance or
    creates one, if none exists.
    """
    def __init__(self):
        super(FlyweightFactory, self).__init__()
        self.flyweights = {}

    def getFlyweight(self, key):
        if not self.flyweight.get(key):
            self.flyweight[key] = ConcreteFlyweight(key)
        return self.flyweight[key]
        

class Client(object):
    """
    Maintains a reference to flyweight(s). Computes or stores the extrinsic 
    state of flyweight(s).
    """
    def __init__(self):
        super(Client, self).__init__()
        