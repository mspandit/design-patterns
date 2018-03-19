import abc


class AbstractClass(metaclass=abc.ABCMeta):
    """Defines abstract *primitive operations* that concrete subclasses define to implement steps of an algorithm. Implements a template method defining the skeleton of an algorithm. The template method calls primitive operations as well as operations defined in AbstractClass or those of other objects."""
    def __init__(self):
        super(AbstractClass, self).__init__()

    @abc.abstractmethod
    def primitive_operation_1(self):
        pass
    
    @abc.abstractmethod
    def primitive_operation_2(self):
        pass

    def template_method(self):
        # Do something
        self.primitive_operation_1()
        # Do something else
        self.primitive_operation_2()
        # And so on


class ConcreteClass(AbstractClass):
    """Implements the primitive operations to carry out subclass-specific steps of the algorithm."""
    def __init__(self):
        super(ConcreteClass, self).__init__()
        
    def primitive_operation_1(self):
        pass
    
    def primitive_operation_2(self):
        pass