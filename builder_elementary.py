import abc
import unittest


class MNISTMLPDirector(object):
    def __init__(self, builder, seed=None):
        super(MNISTMLPDirector, self).__init__()
        self.builder = builder
        self.seed = seed

    def construct(self):
        self.builder.parse_args()
        self.builder.set_seed(self.seed)
        self.builder.initialize_dataset()
        self.builder.build_model()
        return self.builder


class AbstractBuilder(metaclass=abc.ABCMeta):
    def __init__(self):
        super(AbstractBuilder, self).__init__()
        
    @abc.abstractmethod
    def parse_args(self):
        pass
    
    @abc.abstractmethod
    def initialize_dataset(self):
        pass
    
    @abc.abstractmethod
    def set_seed(self):
        pass
    
    @abc.abstractmethod
    def build_model(self):
        pass


from neon.util.argparser import NeonArgparser
from neon.callbacks.callbacks import Callbacks
from neon.data import MNIST
from neon.initializers import Gaussian
from neon.models import Model
from neon.layers import GeneralizedCost, Affine
from neon.optimizers import GradientDescentMomentum
from neon.transforms import (
    Rectlin, 
    Logistic, 
    CrossEntropyBinary, 
    Misclassification
)
from neon.backends import gen_backend
from numpy import random

class NeonBuilder(AbstractBuilder):
    def __init__(self, seed=None):
        super(NeonBuilder, self).__init__()

    def fit(self):
        self.mlp.fit(
            self.dataset.train_iter,
            optimizer=self.optimizer,
            num_epochs=self.args.epochs,
            cost=GeneralizedCost(costfunc=CrossEntropyBinary()),
            callbacks=self.callbacks)
    
    def accuracy(self):
        error_rate = self.mlp.eval(self.dataset.valid_iter, 
                                   metric=Misclassification())
        return (1 - error_rate[0])

    def parse_args(self):
        self.args = NeonArgparser().parse_args()

    def initialize_dataset(self):
        self.dataset = MNIST(path=self.args.data_dir)

    def set_seed(self, seed):
        gen_backend(rng_seed=seed, batch_size=self.args.batch_size)
        random.seed(seed)

    def build_model(self):
        self.mlp = Model(
            layers=[
                Affine(nout=100, init=Gaussian(loc=0.0, scale=0.01),
                       activation=Rectlin()),
                Affine(nout=10, init=Gaussian(loc=0.0, scale=0.01),
                       activation=Logistic(shortcut=True))])
        
        self.optimizer = GradientDescentMomentum(
            0.1, momentum_coef=0.9, stochastic_round=self.args.rounding)
        
        self.callbacks = Callbacks(self.mlp, eval_set=self.dataset.valid_iter, 
                                   **self.args.callback_args)


import argparse
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

class TensorFlowBuilder(AbstractBuilder):
    def __init__(self):
        super(TensorFlowBuilder, self).__init__()
              
    def fit(self):
        self.sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()
        for _ in range(4690):
            batch_xs, batch_ys = self.dataset.train.next_batch(128)
            self.sess.run(self.train_step, 
                          feed_dict={self.x: batch_xs, self.y_: batch_ys})

    def accuracy(self):
        return self.sess.run(self.acc, feed_dict={
                self.x: self.dataset.test.images, 
                self.y_: self.dataset.test.labels
        })

    def parse_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--data_dir', type=str, default='/tmp/mnist_data', 
                            help='Directory for storing input data')
        self.FLAGS, self.unparsed = parser.parse_known_args()

    def initialize_dataset(self):
        self.dataset = input_data.read_data_sets(self.FLAGS.data_dir, 
                                                 one_hot=True)

    def set_seed(self, seed):
        if seed:
            tf.set_random_seed(seed)

    def build_model(self):
        self.x = tf.placeholder(tf.float32, [None, 784])
        W1 = tf.Variable(tf.random_normal_initializer()([784, 100]))
        b1 = tf.Variable(tf.random_normal_initializer()([100]))
        W2 = tf.Variable(tf.random_normal_initializer()([100, 10]))
        b2 = tf.Variable(tf.random_normal_initializer()([10]))
        self.y = tf.matmul(tf.nn.relu(tf.matmul(self.x, W1) + b1), W2) + b2
        self.y_ = tf.placeholder(tf.float32, [None, 10])
        self.train_step = tf.train.MomentumOptimizer(0.1, 0.9).minimize(
            tf.reduce_mean(
                tf.nn.softmax_cross_entropy_with_logits(labels=self.y_, 
                                                        logits=self.y)))
        self.acc = tf.reduce_mean(
            tf.cast(
                tf.equal(tf.argmax(self.y, 1), tf.argmax(self.y_, 1)),
                tf.float32))


class TestMethods(unittest.TestCase):
    def test0(self):
        d = MNISTMLPDirector(NeonBuilder(), 1)
        m = d.construct()
        m.fit()
        self.assertAlmostEqual(0.9746, m.accuracy(), 4)

    def test1(self):
        d = MNISTMLPDirector(TensorFlowBuilder(), 1)
        m = d.construct()
        m.fit()
        self.assertAlmostEqual(0.9275, m.accuracy(), 4)


if __name__ == "__main__":
    unittest.main()