import abc


class Context(object):
    """
    Defines the interface of interest to clients. Maintains an instance of a 
    ConcreteState subclass that defines the current state.
    """
    def __init__(self, state):
        super(Context, self).__init__()
        self.state = state

    def request(self):
        self.state.handle()


class State(metaclass=abc.ABCMeta):
    """
    Defines an interface for encapsulating the behavior associated with a 
    particular state of the Context.
    """
    def __init__(self):
        super(State, self).__init__()
        
    @abc.abstractmethod
    def handle(self):
        pass


class ConcreteState(State):
    """
    Each subclass implements a behavior associated with a state of the Context.
    """
    def __init__(self):
        super(ConcreteState, self).__init__()

    def handle(self):
        pass