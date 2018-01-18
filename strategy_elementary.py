import abc

class SquareRoot(object):
    """Represents a square root operation."""
    def __init__(self, strategy):
        super(SquareRoot, self).__init__()
        self.strategy = strategy

    def evaluate(self, value):
        return self.strategy.evaluate(value)


class SquareRootStrategy(metaclass=abc.ABCMeta):
    """docstring for Strategy."""
    def __init__(self):
        super(SquareRootStrategy, self).__init__()

    @abc.abstractmethod
    def evaluate(self, value):
        pass


class SquareRootStrategyA(object):
    """ uses Python math package to implement square root."""
    def __init__(self):
        super(SquareRootStrategyA, self).__init__()

    def evaluate(self, value):
        import math
        return math.sqrt(value)


class SquareRootStrategyB(object):
    """Uses Newton's Method to implement square root."""
    def __init__(self):
        super(SquareRootStrategyB, self).__init__()

    def evaluate(self, value):
        current = value / 2
        for iter in range(10):
            current = current - (current * current - value) / (2 * current)
        return current


import unittest

class TestMethods(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(TypeError):
            s = SquareRootStrategy()

    def test_1(self):
        node = SquareRoot(SquareRootStrategyA())
        self.assertEqual(2.0, node.evaluate(4.0))

    def test_2(self):
        node = SquareRoot(SquareRootStrategyB())
        self.assertEqual(2.0, node.evaluate(4.0))


if __name__ == '__main__':
    unittest.main()
