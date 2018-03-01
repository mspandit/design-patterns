import unittest
import abc


class AbstractIntermediate(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractIntermediate, self).__init__()

    @abc.abstractmethod
    def compile(self):
        pass


class Intermediate(AbstractIntermediate):
    def __init__(self, compilerTypes):
        super(Intermediate, self).__init__()
        self.compilerTypes = compilerTypes
    
    def compile(self):
        retval = []
        for compilerType in self.compilerTypes:
            if Intel == compilerType:
                retval.append(IntelOperator())
            elif Nvidia == compilerType:
                retval.append(NvidiaOperator())
        return retval


class NvidiaOperator(object):
    def __init__(self):
        super(NvidiaOperator, self).__init__()


class IntelOperator(object):
    def __init__(self):
        super(IntelOperator, self).__init__()


class TensorFlowNode(object):
    def __init__(self, intermediate):
        super(TensorFlowNode, self).__init__()
        self.intermediate = intermediate

    def compile(self):
        return self.intermediate.compile()


class MxNetNode(object):
    def __init__(self, intermediate):
        super(MxNetNode, self).__init__()
        self.intermediate = intermediate

    def compile(self):
        return self.intermediate.compile()


class Nvidia(object):
    def __init__(self):
        super(Nvidia, self).__init__()
        

class Intel(object):
    def __init__(self):
        super(Intel, self).__init__()
        

class TestMethods(unittest.TestCase):
    def test_0(self):
        intermediate = Intermediate([Nvidia]) 
        node = TensorFlowNode(intermediate) 
        compilation = node.compile()
        self.assertEqual(NvidiaOperator, type(compilation[0])) 

    def test_1(self):
        intermediate = Intermediate([Intel])
        node = TensorFlowNode(intermediate)
        compilation = node.compile()
        self.assertEqual(IntelOperator, type(compilation[0]))

    def test_2(self):
        intermediate = Intermediate([Nvidia, Intel])
        node = MxNetNode(intermediate) 
        compilation = node.compile()
        self.assertEqual(NvidiaOperator, type(compilation[0]))
        self.assertEqual(IntelOperator, type(compilation[1]))


if __name__ == "__main__":
    unittest.main() 
