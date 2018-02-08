def simple_generator():
    yield 0
    yield 1
    yield 4

def generator():
    for i in range(3):
        yield i * i

import unittest

class TestMethods(unittest.TestCase):
    def test0(self):
        self.assertEqual([0, 1, 4], [result for result in simple_generator()])

    def test1(self):
        self.assertEqual([0, 1, 4], [result for result in generator()])

if __name__ == '__main__':
    unittest.main()
