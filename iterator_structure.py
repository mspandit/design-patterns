import abc


class Aggregate(metaclass=abc.ABCMeta):
    """Defines an interface for creating an Iterator object."""
    def __init__(self):
        super(Aggregate, self).__init__()

    @abc.abstractmethod
    def create_iterator(self):
        pass


class ConcreteAggregate(Aggregate):
    """
    Implements the Iterator creation interface to return an instance of the
    proper ConcreteIterator.
    """
    def __init__(self):
        super(ConcreteAggregate, self).__init__()

    def create_iterator(self):
        return ConcreteIterator(self)


class Iterator(metaclass=abc.ABCMeta):
    """Defines an interface for accessing and traversing elements."""
    def __init__(self):
        super(Iterator, self).__init__()

    @abc.abstractmethod
    def first(self):
        pass

    @abc.abstractmethod
    def next(self):
        pass

    @abc.abstractmethod
    def is_done(self):
        pass

    @abc.abstractmethod
    def current_item(self):
        pass


class ConcreteIterator(Iterator):
    """
    Implements the Iterator interface. Keeps track of the current position in
    the traversal of the aggregate.
    """
    def __init__(self, aggregate):
        super(ConcreteIterator, self).__init__()
        self.aggregate = aggregate
