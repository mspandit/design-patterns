import abc


class Abstraction(metaclass=abc.ABCMeta):
    """
    Defines an abstraction's interface. Maintains a reference to an object
    of type Implementor.
    """
    def __init__(self, implementation):
        super(Abstraction, self).__init__()
        self.implementation = implementation

    @abc.abstractmethod
    def operations(self):
        self.implementation.operation_implementation()


class RefinedAbstraction(Abstraction):
    """Extends the interface defined by Abstraction."""
    def __init__(self):
        super(RefinedAbstraction, self).__init__()


class Implementor(metaclass=abc.ABCMeta):
    """
    Defines the interface for implementation classes. This interface doesn't
    have to correspond exactly to Abstraction's interface; in fact the two
    interfaces can be quite different. Typically the Implementor interface
    provides only primitive operations, and Abstraction defines higher-level
    operations based on these primitives.
    """
    def __init__(self):
        super(Implementor, self).__init__()

    @abc.abstractmethod
    def operation_implementation(self):
        pass


class ConcreteImplementorA(Implementor):
    """
    Implements the Implementor interface and defines its concrete
    implementation.
    """
    def __init__(self):
        super(ConcreteImplementorA, self).__init__()

    def operation_implementation(self):
        pass


class ConcreteImplementorB(Implementor):
    """
    Implements the Implementor interface and defines its concrete
    implementation.
    """
    def __init__(self):
        super(ConcreteImplementorB, self).__init__()

    def operation_implementation(self):
        pass
