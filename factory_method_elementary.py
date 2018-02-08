import abc
from visitor_elementary import Integer, Addition


class AbstractCreator(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractCreator, self).__init__()

    @abc.abstractmethod
    def create(self, key):
        pass


class Creator(AbstractCreator):
    def __init__(self):
        super(Creator, self).__init__()

    def create(self, key):
        if int == type(key):
            return Integer(key)
        elif '+' == key:
            return Addition([])


import unittest


class TestMethods(unittest.TestCase):
    def test0(self):
        c = Creator()

    def test1(self):
        creator = Creator()
        four = creator.create(4)
        self.assertEqual(4, four.value)
        five = creator.create(5)
        self.assertEqual(5, five.value)

    def test2(self):
        creator = Creator()
        addition = creator.create('+')
        self.assertEqual(Addition, type(addition))
        

if __name__ == "__main__":
    unittest.main()