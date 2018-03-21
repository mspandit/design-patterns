import abc


class Director(object):
    """Constructs an object using the Builder interface."""
    def __init__(self, builder):
        super(Director, self).__init__()
        self.builder = builder
        
    def construct(self):
        for obj in self.structure:
            self.builder.build_part()


class Builder(metaclass=abc.ABCMeta):
    """
    Specifies an abstract interface for creating parts of a Product object.
    """
    def __init__(self):
        super(Builder, self).__init__()

    @abc.abstractmethod
    def build_part(self):
        """Called by Director"""
        pass

    @abc.abstractmethod
    def get_result(self):
        """Called by Client (creator of ConcreteBuilder and Director)"""
        pass


class ConcreteBuilder(Builder):
    """
    Constructs and assembles parts of the product by implementing the Builder 
    interface. Defines and keeps track of the representation it creates. 
    Provides an interface for retrieving the product.
    """
    def __init__(self):
        super(ConcreteBuilder, self).__init__()

    def build_part(self):
        pass

    def get_result(self):
        pass


class Product(object):
    """
    Represents the complex object under construction. ConcreteBuilder builds the 
    product's internal representation and defines the process by which it's 
    assembled. Includes classes that define the constituent parts, including 
    interfaces for assembling the parts into the final result.
    """
    def __init__(self):
        super(Product, self).__init__()

        