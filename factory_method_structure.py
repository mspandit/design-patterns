import abc


class Product(metaclass=abc.ABCMeta):
    """Defines the interface of objects the factory method creates."""
    def __init__(self):
        super(Product, self).__init__()


class ConcreteProduct(Product):
    """Implements the Product interface"""
    def __init__(self):
        super(ConcreteProduct, self).__init__()


class Creator(metaclass=abc.ABCMeta):
    """
    Declares the factory method, which returns an object of type Product.
    Creator may also define a default implementation of the factory method that
    returns a default ConcreteProduct object.
    """
    def __init__(self):
        super(Creator, self).__init__()

    @abc.abstractmethod
    def factory_method(self):
        pass


class ConcreteCreator(Creator):
    """
    Overrides the factory method to return an instance of a ConcreteProduct.
    """
    def __init__(self):
        super(ConcreteCreator, self).__init__()

        