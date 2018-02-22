import unittest
import abc


class AbstractAnswerer(metaclass=abc.ABCMeta):
    def __init__(self, successor):
        super(AbstractAnswerer, self).__init__()
        self.successor = successor
    
    @abc.abstractmethod
    def askQuestion(self, type):
        pass


class Engineer(AbstractAnswerer):
    def __init__(self, successor=None):
        super(Engineer, self).__init__(successor)
    
    def askQuestion(self, qtype):
        if "Technical" == qtype:
            return "Answered!"
        elif self.successor:
            return self.successor.askQuestion(qtype)

class Lawyer(AbstractAnswerer):
    def __init__(self, successor=None):
        super(Lawyer, self).__init__(successor)
        
    def askQuestion(self, qtype):
        if "Legal" == qtype:
            return "Answered!"
        elif self.successor:
            return self.successor.askQuestion(qtype)


class Manager(AbstractAnswerer):
    def __init__(self, successor=None):
        super(Manager, self).__init__(successor)

    def askQuestion(self, qtype):
        if "Managerial" == qtype:
            return "Answered!"
        elif self.successor:
            return self.successor.askQuestion(qtype)


class TestMethods(unittest.TestCase):
    def test0(self):
        e = Engineer()
        self.assertEqual("Answered!", e.askQuestion("Technical"))

    def test1(self):
        l = Lawyer() 
        self.assertEqual("Answered!", l.askQuestion("Legal"))

    def test2(self):
        e = Engineer(Lawyer())
        self.assertEqual("Answered!", e.askQuestion("Technical"))
        self.assertEqual("Answered!", e.askQuestion("Legal"))

    def test3(self):
        m = Manager(Engineer(Lawyer()))
        self.assertEqual("Answered!", m.askQuestion("Managerial"))
        self.assertEqual("Answered!", m.askQuestion("Technical"))
        self.assertEqual("Answered!", m.askQuestion("Legal"))


if __name__ == "__main__":
    unittest.main()