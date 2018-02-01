import abc


class AbstractIterator(metaclass=abc.ABCMeta):
    def __init__(self, aggregate):
        super(AbstractIterator, self).__init__()
        self.aggregate = aggregate

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


class Iterator(AbstractIterator):
    def __init__(self, aggregate):
        super(Iterator, self).__init__(aggregate)
        self.row = 0
        self.column = 0

    def first(self):
        self.row = 0
        self.column = 0

    def next(self):
        self.column += 1
        if self.column >= len(self.aggregate.contents[self.row]):
            self.column = 0
            self.row += 1

    def is_done(self):
        if self.row >= len(self.aggregate.contents):
            return True
        else:
            return False

    def current_item(self):
        return self.aggregate.contents[self.row][self.column]


class ReverseIterator(AbstractIterator):
    def __init__(self, aggregate):
        super(ReverseIterator, self).__init__(aggregate)
        self.row = len(self.aggregate.contents) - 1
        self.column = len(self.aggregate.contents[-1]) - 1

    def first(self):
        self.row = len(self.aggregate.contents) - 1
        self.column = len(self.aggregate.contents[-1]) - 1

    def next(self):
        self.column -= 1
        if self.column < 0:
            self.row -= 1
            self.column = len(self.aggregate.contents[self.row]) - 1

    def is_done(self):
        if self.row < 0:
            return True
        else:
            return False

    def current_item(self):
        return self.aggregate.contents[self.row][self.column]


class PythonIterator(object):
    def __init__(self, aggregate):
        super(PythonIterator, self).__init__()
        self.aggregate = aggregate
        self.row = 0
        self.column = 0

    def __next__(self):
        if self.row >= len(self.aggregate.contents):
            raise StopIteration
        else:
            current = self.aggregate.contents[self.row][self.column]
            self.column += 1
            if self.column >= len(self.aggregate.contents[self.row]):
                self.column = 0
                self.row += 1
            return current


class Aggregate(metaclass=abc.ABCMeta):
    """Defines an interface for creating various iterator objects."""
    def __init__(self):
        super(Aggregate, self).__init__()

    @abc.abstractmethod
    def create_iterator(self):
        pass


class DataSet(Aggregate):
    def __init__(self, contents):
        super(DataSet, self).__init__()
        self.contents = contents

    def __iter__(self):
        return PythonIterator(self)

    def create_iterator(self, reverse=False):
        if reverse:
            return ReverseIterator(self)
        else:
            return Iterator(self)


import unittest
import math

class TestMethods(unittest.TestCase):
    def test0(self):
        d = DataSet([[1, None, math.pi], [4, 5, 6], [7, 8, 9]])

    def test1(self):
        d = DataSet([[1, None, math.pi], [4, 5, 6], [7, 8, 9]])
        i = d.create_iterator()
        i.first()
        results = []
        while False == i.is_done():
            results.append(i.current_item())
            i.next()
        self.assertEqual([1, None, math.pi, 4, 5, 6, 7, 8, 9], results)
        i = d.create_iterator(reverse=True)
        i.first()
        results = []
        while False == i.is_done():
            results.append(i.current_item())
            i.next()
        self.assertEqual([9, 8, 7, 6, 5, 4, math.pi, None, 1], results)

    def test3(self):
        d = DataSet([[1, None, math.pi], [4, 5, 6], [7, 8, 9]])
        results = []
        for e in d:
            results.append(e)
        self.assertEqual([1, None, math.pi, 4, 5, 6, 7, 8, 9], results)


if __name__ == "__main__":
    unittest.main()
