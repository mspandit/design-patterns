import abc


class Mediator(metaclass=abc.ABCMeta):
    """Defines an interface for communicating with Colleague objects."""
    def __init__(self):
        super(Mediator, self).__init__()


class ConcreteMediator(Mediator):
    """
    Implements cooperative behavior by coordinating Colleague objects.
    Knows and maintains its colleagues
    """
        
    def __init__(self, colleague1, colleague2):
        super(ConcreteMediator, self).__init__()
        self.colleague1 = colleague1
        self.colleague2 = colleague2


class Colleague1(object):
    """
    Knows its Mediator object.
    Communicates with its mediator whenever it would have otherwise communicated
    with another colleague.
    """
        
    def __init__(self, mediator):
        super(Colleague1, self).__init__()
        self.mediator = mediator


class Colleague2(object):
    """
    Knows its Mediator object.
    Communicates with its mediator whenever it would have otherwise communicated
    with another colleague.
    """
        
    def __init__(self, mediator):
        super(Colleague1, self).__init__()
        self.mediator = mediator
        
        
        