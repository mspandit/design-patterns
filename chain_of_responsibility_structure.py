import abc


class Handler(metaclass=abc.ABCMeta):
    """Defines an interface for handling requests. Implements the successor link."""
    def __init__(self, successor):
        super(Handler, self).__init__()
        self.successor = successor

    @abc.abstractmethod
    def handleRequest(self):
        pass


class ConcreteHandler1(Handler):
    """
    Handles requests it is responsible for. Can access its successor. 
    If the ConcreteHandler can handle the request, it does so; otherwise it
    forwards the request to its successor.
    """
    def __init__(self, successor):
        super(ConcreteHandler1, self).__init__(successor)

    def handleRequest(self):
        """Handle request if possible, or delegate to successor."""
        pass