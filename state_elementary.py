import abc

import unittest


class DataSet(object):
    def __init__(self, initial_state=None):
        super(DataSet, self).__init__()
        self.trainingState = DataSetTraining()
        self.validatingState = DataSetValidating()
        self.testingState = DataSetTesting()
        if initial_state is None:
            self.state = self.trainingState
        else:
            self.state = initial_state

    def train(self):
        """Switch state to training iterator."""
        self.state = self.trainingState

    def validate(self):
        """Switch state to validation iterator"""
        self.state = self.validatingState

    def test(self):
        """Switch state to testing iterator"""
        self.state = self.testingState

    def next(self):
        return self.state.next()


class DataSetState(metaclass=abc.ABCMeta):
    def __init__(self):
        super(DataSetState, self).__init__()
    
    @abc.abstractmethod
    def next(self):
        pass


class DataSetTraining(DataSetState):
    def __init__(self):
        super(DataSetTraining, self).__init__()
        self.data = [
            ("train_x_1", "train_y_1"),
            ("train_x_2", "train_y_2"),
            ("train_x_3", "train_y_3")
        ]
        self.data_index = 0

    def next(self):
        if self.data_index >= len(self.data):
            return (None, None)
        else:
            self.data_index += 1
            return (self.data[self.data_index - 1])


class DataSetValidating(DataSetState):
    def __init__(self):
        super(DataSetValidating, self).__init__()
        self.data = [
            ("validate_x_1", "validate_y_1"),
            ("validate_x_2", "validate_y_2"),
            ("validate_x_3", "validate_y_3")
        ]
        self.data_index = 0

    def next(self):
        if self.data_index >= len(self.data):
            return (None, None)
        else:
            self.data_index += 1
            return (self.data[self.data_index - 1])


class DataSetTesting(DataSetState):
    def __init__(self):
        super(DataSetTesting, self).__init__()
        self.data = [
            ("test_x_1", "test_y_1"),
            ("test_x_2", "test_y_2"),
            ("test_x_3", "test_y_3")
        ]
        self.data_index = 0

    def next(self):
        if self.data_index >= len(self.data):
            return (None, None)
        else:
            self.data_index += 1
            return (self.data[self.data_index - 1])


class TestMethods(unittest.TestCase):
    def test0(self):
        d = DataSet() 
        d.train() 
        x, y = d.next() 
        self.assertEqual("train_x_1", x) 
        self.assertEqual("train_y_1", y)
        x, y = d.next()
        self.assertEqual("train_x_2", x)
        self.assertEqual("train_y_2", y)
        d.validate() 
        x, y = d.next()
        self.assertEqual("validate_x_1", x)
        self.assertEqual("validate_y_1", y)
        x, y = d.next()
        self.assertEqual("validate_x_2", x)
        self.assertEqual("validate_y_2", y)
        d.test() 
        x, y = d.next()
        self.assertEqual("test_x_1", x)
        self.assertEqual("test_y_1", y)
        x, y = d.next()
        self.assertEqual("test_x_2", x)
        self.assertEqual("test_y_2", y)
        d.train()
        x, y = d.next()
        self.assertEqual("train_x_3", x) 
        self.assertEqual("train_y_3", y)
        d.validate()
        x, y = d.next()
        self.assertEqual("validate_x_3", x)
        self.assertEqual("validate_y_3", y)
        d.test()
        x, y = d.next()
        self.assertEqual("test_x_3", x) 
        self.assertEqual("test_y_3", y)


if __name__ == "__main__":
    unittest.main()
        