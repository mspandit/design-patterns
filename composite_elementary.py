import abc

class Expression(metaclass=abc.ABCMeta):
    """Abstract class."""
    def __init__(self):
        super(Expression, self).__init__()
        self.children = []

    @abc.abstractmethod
    def evaluate(self):
        pass

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def get_child(self, child_index):
        return self.children[child_index]


class Addition(Expression):
    """Represents an addition operation."""
    def __init__(self):
        super(Addition, self).__init__()

    def evaluate(self):
        sum = 0
        for child in self.children:
            sum += child.evaluate()
        return sum


class Subtraction(Expression):
    """Represents a subtraction operation."""
    def __init__(self):
        super(Subtraction, self).__init__()

    def add(self, component):
        if len(self.children) > 1:
            raise Exception("Can't add more than two components.")
        super(Subtraction, self).add(component)

    def evaluate(self):
        return self.children[0].evaluate() - self.children[1].evaluate()


class Multiplication(Expression):
    """Represents a multiplication operation."""
    def __init__(self):
        super(Multiplication, self).__init__()

    def evaluate(self):
        product = 1
        for child in self.children:
            product *= child.evaluate()
        return product


class Number(Expression):
    def __init__(self, value):
        super(Number, self).__init__()
        self.value = value

    def evaluate(self):
        return self.value


import unittest

class TestMethods(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(TypeError):
            e = Expression()

    def test_1(self):
        """ (1) """
        self.assertEqual(1, Number(1).evaluate())

    def test_2(self):
        """ (1 + 2) """
        n1 = Number(1)
        n2 = Number(2)
        add = Addition()
        add.add(n1)
        add.add(n2)
        self.assertEqual(3, add.evaluate())

    def test_3(self):
        """ (1 - 2) """
        sub = Subtraction()
        sub.add(Number(1))
        sub.add(Number(2))
        with self.assertRaises(Exception):
            sub.add(Number(3))
        self.assertEqual(-1, sub.evaluate())

    def test_4(self):
        """ ((4 + 2) * (3 - 1)) """
        add = Addition()
        add.add(Number(4))
        add.add(Number(2))
        sub = Subtraction()
        sub.add(Number(3))
        sub.add(Number(1))
        mul = Multiplication()
        mul.add(add)
        mul.add(sub)
        self.assertEqual(12, mul.evaluate())

if __name__ == '__main__':
    unittest.main()
