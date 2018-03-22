import unittest
from neon.util.argparser import NeonArgparser
from neon.data import MNIST
from neon.callbacks.callbacks import Callbacks
from neon.initializers import Gaussian
from neon.layers import GeneralizedCost, Affine
from neon import models
from neon.optimizers import GradientDescentMomentum
from neon.transforms import (Rectlin, Logistic, CrossEntropyBinary,
                             Misclassification)
from numpy import random
from neon.backends import gen_backend
import abc


class Model(metaclass=abc.ABCMeta):
    def __init__(self, args):
        super(Model, self).__init__()
        self.dataset = MNIST(path=args.data_dir)
        self.mlp = models.Model(
            layers=[
                Affine(nout=100, init=Gaussian(loc=0.0, scale=0.1),
                       activation=self.get_first_layer_activation()),
                Affine(nout=10, init=Gaussian(loc=0.0, scale=0.1),
                       activation=Logistic(shortcut=True))])
        self.optimizer = GradientDescentMomentum(
            0.1, momentum_coef=0.9, stochastic_round=args.rounding)
        self.callbacks = Callbacks(self.mlp, eval_set=self.dataset.valid_iter, **args.callback_args)
        self.args = args

    def fit(self):
        self.mlp.fit(
            self.dataset.train_iter,
            optimizer=self.optimizer,
            num_epochs=self.args.epochs,
            cost=GeneralizedCost(costfunc=CrossEntropyBinary()),
            callbacks=self.callbacks)

    def evaluate(self):
        error_rate = self.mlp.eval(self.dataset.valid_iter, metric=Misclassification())
        return (1 - error_rate[0])

    @abc.abstractmethod
    def get_first_layer_activation(self):
        pass


class RectlinModel(Model):
    def __init__(self, args):
        super(RectlinModel, self).__init__(args)

    def get_first_layer_activation(self):
        return Rectlin()


class LogisticModel(Model):
    def __init__(self, args):
        super(LogisticModel, self).__init__(args)

    def get_first_layer_activation(self):
        return Logistic(shortcut=True)


class TestMethods(unittest.TestCase):
    def test0(self):
        args = NeonArgparser().parse_args()
        random.seed(1)
        gen_backend(rng_seed=1, batch_size=args.batch_size)
        mlp = RectlinModel(args)
        mlp.fit()
        self.assertAlmostEqual(0.97, mlp.evaluate(), 2) 

    def test1(self):
        args = NeonArgparser().parse_args()
        random.seed(1)
        gen_backend(rng_seed=1, batch_size=args.batch_size)
        mlp = LogisticModel(args)
        mlp.fit()
        self.assertAlmostEqual(0.87, mlp.evaluate(), 2) 


if __name__ == "__main__":
    unittest.main()