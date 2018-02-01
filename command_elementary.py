import abc
import copy


class Modification(metaclass=abc.ABCMeta):
    """Interface for modifications to a model."""
    def __init__(self):
        super(Modification, self).__init__()

    @abc.abstractmethod
    def apply(self):
        pass

    @abc.abstractmethod
    def undo(self):
        pass


class Increment(Modification):
    """Modifies a model by incrementing its weights."""
    def __init__(self, model, deltas):
        super(Increment, self).__init__()
        self.model = model
        self.deltas = copy.copy(deltas)

    def apply(self):
        self.model._increment(self.deltas)

    def undo(self):
        self.model._increment([-1.0 * delta for delta in self.deltas])


class Model(object):
    """A very very simple model."""
    def __init__(self, weights):
        super(Model, self).__init__()
        self.weights = weights
        self.modifications = []

    def _increment(self, deltas):
        new_weights = []
        for weight, delta in zip(self.weights, deltas):
            new_weights.append(weight + delta)
        self.weights = new_weights

    def increment(self, deltas):
        mod = Increment(self, deltas)
        mod.apply()
        self.modifications.append(mod)
        return len(self.modifications)

    def undo(self):
        self.modifications.pop(-1).undo()

    def revert(self, length):
        while length < len(self.modifications):
            self.undo()


import unittest

class TestMethods(unittest.TestCase):
    def test0(self):
        m = Model([1.5, 3.0])
        self.assertEqual([1.5, 3.0], m.weights)

    def test1(self):
        m = Model([4.5, 88.0])
        m.increment([1.0, 1.0])
        self.assertEqual([5.5, 89.0], m.weights)

    def test2(self):
        m = Model([45.6, 12.3])
        m.increment([1.0, -1.0])
        self.assertEqual([46.6, 11.3], m.weights)
        m.undo()
        self.assertEqual([45.6, 12.3], m.weights)

    def test3(self):
        m = Model([4872.3, 346.782, 46.0])
        m.increment([1.0, -1.0, 1.0])
        m.increment([-1.0, 1.0, -1.0])
        m.undo()
        m.undo()
        self.assertEqual([4872.3, 346.782, 46.0], m.weights)

    def test4(self):
        m = Model([467.08, 172.478, 6.4])
        checkpoint = m.increment([1.0, -1.0, 1.0])
        m.increment([1.0, 1.0, 1.0])
        m.increment([1.0, 1.0, 1.0])
        m.increment([1.0, 1.0, 1.0])
        m.increment([1.0, 1.0, 1.0])
        m.revert(checkpoint)
        self.assertEqual([468.08, 171.478, 7.4], m.weights)


if __name__ == "__main__":
    unittest.main()
