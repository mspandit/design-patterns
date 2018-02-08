import unittest


class Number(object):
    class Statistics(object):
        def __init__(self):
            self.count = 0
            self.sum = 0
    
    _statistics = None
            
    def __init__(self, value):
        super(Number, self).__init__()
        self.value = value
        Number.statistics().count += 1
        Number.statistics().sum += value
    
    @staticmethod
    def statistics():
        if Number._statistics is None:
            Number._statistics = Number.Statistics()
        return Number._statistics


class TestMethods(unittest.TestCase):
    def test0(self):
        n1 = Number(1)
        n2 = Number(2)
        self.assertEqual(2, Number.statistics().count) 
        self.assertEqual(3, Number.statistics().sum)


if __name__ == "__main__":
    unittest.main()