import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    """
    Declares an interface for operations that create abstract product objects.
    """
    def __init__(self):
        super(AbstractFactory, self).__init__()

    @abc.abstractmethod
    def create_product_a(self):
        pass

    @abc.abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    """Implements the operations to create concrete product objects."""
    def __init__(self):
        super(ConcreteFactory1, self).__init__()

    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory2(AbstractFactory):
    """Implements the operations to create concrete product objects."""
    def __init__(self):
        super(ConcreteFactory1, self).__init__()

    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class AbstractProductA(metaclass=abc.ABCMeta):
    """
    Declares an interface for a type of product object.
    """
    def __init__(self):
        super(AbstractProduct, self).__init__()


class ProductA1(AbstractProductA):
    """
    Defines a product object to be created by the corresponding concrete
    factory. Implements the AbstractProductA interface.
    """
    def __init__(self):
        super(ProductA1, self).__init__()


class ProductA2(AbstractProductA):
    """
    Defines a product object to be created by the corresponding concrete
    factory. Implements the AbstractProductA interface.
    """
    def __init__(self):
        super(ProductA2, self).__init__()


class AbstractProductB(metaclass=abc.ABCMeta):
    """
    Declares an interface for a type of product object.
    """
    def __init__(self):
        super(AbstractProductB, self).__init__()


class ProductB1(AbstractProductB):
    """
    Defines a product object to be created by the corresponding concrete
    factory. Implements the AbstractProductB interface.
    """
    def __init__(self):
        super(ProductB1, self).__init__()


class ProductB2(AbstractProductB):
    """
    Defines a product object to be created by the corresponding concrete
    factory. Implements the AbstractProductB interface.
    """
    def __init__(self):
        super(ProductB2, self).__init__()

class Client(object):
    """
    Uses only interfaces declared by AbstractFactory and AbstractProduct classes.
    """
    def __init__(self, abstract_factory):
        super(Client, self).__init__()
        self.abstract_factory = abstract_factory
