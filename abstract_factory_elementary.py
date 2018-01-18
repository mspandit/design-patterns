import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractFactory, self).__init__()

    @abc.abstractmethod
    def random_array(self, length):
        pass

    @abc.abstractmethod
    def random_matrix(self, rows, columns):
        pass


import random

class PythonFactory(AbstractFactory):
    def __init__(self):
        super(PythonFactory, self).__init__()
        random.seed(4)

    def random_array(self, length):
        return PythonArray(length)

    def random_matrix(self, rows, columns):
        return PythonMatrix(rows, columns)


import numpy

class NumpyFactory(AbstractFactory):
    def __init__(self):
        super(NumpyFactory, self).__init__()
        numpy.random.seed(4)

    def random_array(self, length):
        return NumpyArray(length)

    def random_matrix(self, rows, columns):
        return NumpyMatrix(rows, columns)


class AbstractArray(metaclass=abc.ABCMeta):
    def __init__(self, length):
        super(AbstractArray, self).__init__()
        self.length = length

    @abc.abstractmethod
    def multiply(self, other):
        pass

    def length(arg):
        return self.length


class PythonArray(AbstractArray):
    def __init__(self, length):
        super(PythonArray, self).__init__(length)
        self.array = [random.random() for _ in range(length)]

    def multiply(self, other):
        if self.length == other.length:
            result = PythonArray(self.length)
            result.array = [e[0] * e[1] for e in zip(self.array, other.array)]
            return result
        else:
            raise Exception("Lengths must be equal for elementwise multiplication.")


class NumpyArray(AbstractArray):
    def __init__(self, length):
        super(NumpyArray, self).__init__(length)
        self.array = numpy.random.rand(length)

    def length(self):
        return self.length

    def multiply(self, other):
        if self.length == other.length:
            result = NumpyArray(self.length)
            result.array = numpy.multiply(self.array, other.array)
            return result
        else:
            raise Exception("Lengths must be equal for elementwise multiplication.")


class AbstractMatrix(metaclass=abc.ABCMeta):
    def __init__(self, rows, columns):
        super(AbstractMatrix, self).__init__()
        self.rows = rows
        self.columns = columns

    @abc.abstractmethod
    def multiply(self, other):
        pass

    def rows(self):
        return self.rows

    def columns(self):
        return self.columns


class PythonMatrix(AbstractMatrix):
    def __init__(self, rows, columns):
        super(PythonMatrix, self).__init__(rows, columns)
        self.matrix = [[random.random() for _ in range(columns)] for _ in range(rows)]

    def multiply(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = PythonMatrix(self.rows, self.columns)
            result.matrix = [[e[0] * e[1] for e in zip(f[0], f[1])] for f in zip(self.matrix, other.matrix)]
            return result
        else:
            raise Exception("Rows and columns must be equal for elementwise multiplication.")


class NumpyMatrix(AbstractMatrix):
    def __init__(self, rows, columns):
        super(NumpyMatrix, self).__init__(rows, columns)
        self.matrix = numpy.random.rand(rows, columns)

    def multiply(self, other):
        if self.rows == other.rows and self.columns == other.columns:
            result = NumpyMatrix(self.rows, self.columns)
            result.matrix = numpy.multiply(self.matrix, other.matrix)
            return result
        else:
            raise Exception("Rows and columns must be equal for elementwise multiplication.")


class Client(object):
    def __init__(self, concrete_factory):
        super(Client, self).__init__()
        self.concrete_factory = concrete_factory

    def array_element_multiply(self):
        m1 = self.concrete_factory.random_array(4)
        m2 = self.concrete_factory.random_array(4)
        return m1.multiply(m2)

    def matrix_element_multiply(self):
        m1 = self.concrete_factory.random_matrix(2, 2)
        m2 = self.concrete_factory.random_matrix(2, 2)
        return m1.multiply(m2)


import unittest

class TestMethods(unittest.TestCase):
    def test_0(self):
        with self.assertRaises(TypeError):
            a = AbstractMatrix()
        with self.assertRaises(TypeError):
            a = AbstractArray()
        with self.assertRaises(TypeError):
            a = AbstractFactory()

    def test_1(self):
        cl = Client(PythonFactory())
        self.assertEqual([0.015700761273869882, 0.04143055234711512, 0.3635636611609339, 0.12404791858043453], cl.array_element_multiply().array)

    def test_2(self):
        cl = Client(NumpyFactory())
        self.assertEqual([0.6747245929255007, 0.11825114068969668, 0.9496068931940951, 0.004453486064913785], cl.array_element_multiply().array.tolist())

    def test_3(self):
        cl = Client(PythonFactory())
        self.assertEqual([[0.015700761273869882, 0.04143055234711512], [0.3635636611609339, 0.12404791858043453]], cl.matrix_element_multiply().matrix)

    def test_4(self):
        cl = Client(NumpyFactory())
        self.assertEqual([[0.6747245929255007, 0.11825114068969668], [0.9496068931940951, 0.004453486064913785]], cl.matrix_element_multiply().matrix.tolist())

if __name__ == '__main__':
    unittest.main()
