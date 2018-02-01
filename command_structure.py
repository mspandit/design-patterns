import abc

class Command(abc.ABCMeta):
    """Declares an interface for executing an operation."""
    def __init__(self):
        super(Command, self).__init__()

    @abc.abstractmethod
    def execute():
        pass

class ConcreteCommand(Command):
    """
    Defines a binding between a Receiver object and an action.
    Implements execute() by invoking the corresponding operation(s) on Receiver.
    """
    def __init__(self, receiver):
        super(ConcreteCommand, self).__init__()
        self.receiver = receiver

    def execute():
        self.receiver.action()


class Client(object):
    """Creates a ConcreteCommand object and sets its receiver."""
    def __init__(self, invoker):
        super(Client, self).__init__()
        self.invoker = invoker
        invoker.store_command(ConcreteCommand(Receiver()))


class Invoker(object):
    """Asks the command to carry out the request."""
    def __init__(self):
        super(Invoker, self).__init__()

    def store_command(self, command):
        self.command = command

    def invoke(self):
        self.command.execute()


class Receiver(object):
    """
    Knows how to perform the operations associated with carrying out a request.
    Any class may serve as a Receiver.
    """
    def __init__(self):
        super(Receiver, self).__init__()
