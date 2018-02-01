import abc


class AbstractVisitor(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractVisitor, self).__init__()

    @abc.abstractmethod
    def visit_integer(self, integer):
        pass

    @abc.abstractmethod
    def visit_addition(self, addition):
        pass


class Evaluator(AbstractVisitor):
    def __init__(self):
        super(Evaluator).__init__()
        self.value = 0

    def visit_integer(self, integer):
        self.value = integer.value

    def visit_addition(self, addition):
        self.value = sum([a.value for a in addition.addends])


class Writer(AbstractVisitor):
    def __init__(self):
        super(Writer, self).__init__()
        self.value = ""

    def visit_integer(self, integer):
        self.value = "%d" % integer.value

    def visit_addition(self, addition):
        self.value = "(%s)" % " + ".join([str(v.value) for v in addition.addends])


class Element(metaclass=abc.ABCMeta):
    def __init__(self):
        super(Element).__init__()

    @abc.abstractmethod
    def accept(self, visitor):
        pass


class Integer(Element):
    def __init__(self, value):
        super(Integer, self).__init__()
        self.value = value

    def accept(self, visitor):
        visitor.visit_integer(self)


class Addition(Element):
    def __init__(self, addends):
        super(Addition, self).__init__()
        self.addends = addends

    def accept(self, visitor):
        visitor.visit_addition(self)


import unittest
class TestMethods(unittest.TestCase):
    def test0(self):
        four = Integer(4)
        six = Integer(6)

    def test1(self):
        five = Integer(5)
        seven = Integer(7)
        addition = Addition([five, seven])

    def test2(self):
        three = Integer(3)
        eight = Integer(8)
        addition = Addition([three, eight])
        evaluator = Evaluator()
        addition.accept(evaluator)
        self.assertEqual(11, evaluator.value)
        writer = Writer()
        addition.accept(writer)
        self.assertEqual("(3 + 8)", writer.value)


if __name__ == '__main__':
    unittest.main()
