import abc

class Component(metaclass=abc.ABCMeta):
    """
    Defines the interface for objects that can have responsibilities added to
    them dynamically.
    """
    def __init__(self):
        super(Component, self).__init__()

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    """
    Defines an object to which additional responsibilities can be added.
    """
    def __init__(self):
        super(ConcreteComponent, self).__init__()

    def operation(self):
        # Do something useful here
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintains a reference to a component object and defines an interface that
    conforms to Component's interface.
    """
    def __init__(self, component):
        super(Decorator, self).__init__()
        self.component = component

    def operation(self):
        return self.component.operation()


class ConcreteDecoratorA(Decorator):
    """Adds responsibilities to the component."""
    def __init__(self, component, addedState):
        super(ConcreteDecoratorA, self).__init__(component)
        self.addedState = addedState

    def operation(self):
        pass


class ConcreteDecoratorB(Decorator):
    """Adds responsibilities to the component."""
    def __init__(self, component, addedBehavior):
        super(ConcreteDecoratorB, self).__init__(component)
        self.addedBehavior = addedBehavior

    def operation(self):
        super(ConcreteDecoratorB, self).operation()
        self.addedBehavior()
