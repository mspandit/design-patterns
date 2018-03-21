import unittest

from neon.util.argparser import NeonArgparser
from neon.callbacks.callbacks import Callbacks
from neon.data import MNIST
from neon.initializers import Gaussian
from neon.models import Model
from neon.layers import GeneralizedCost, Affine
from neon.optimizers import GradientDescentMomentum
from neon.transforms import (Rectlin, Logistic, CrossEntropyBinary, Misclassification)

class NeonMNISTMLP(object):
    def __init__(self):
        super(NeonMNISTMLP, self).__init__()
        self.args = NeonArgparser().parse_args()
        self.dataset = MNIST(path=self.args.data_dir)
        self.mlp = Model(
            layers=[
                Affine(nout=100, init=Gaussian(loc=0.0, scale=0.01),
                       activation=Rectlin()),
                Affine(nout=10, init=Gaussian(loc=0.0, scale=0.01),
                       activation=Logistic(shortcut=True))])
        
        self.optimizer = GradientDescentMomentum(
            0.1, momentum_coef=0.9, stochastic_round=self.args.rounding)
        
        self.callbacks = Callbacks(self.mlp, eval_set=self.dataset.valid_iter, **self.args.callback_args)

    def fit(self):
        self.mlp.fit(
            self.dataset.train_iter,
            optimizer=self.optimizer,
            num_epochs=self.args.epochs,
            cost=GeneralizedCost(costfunc=CrossEntropyBinary()),
            callbacks=self.callbacks)
    
    def accuracy(self):
        error_rate = self.mlp.eval(self.dataset.valid_iter, metric=Misclassification())
        return (1 - error_rate[0])


import argparse
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

class TensorFlowMNISTMLP(object):
    def __init__(self):
        super(TensorFlowMNISTMLP, self).__init__()
        parser = argparse.ArgumentParser()
        parser.add_argument('--data_dir', type=str, default='/tmp/mnist_data', help='Directory for storing input data')
        self.FLAGS, self.unparsed = parser.parse_known_args()
        self.dataset = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
        self.x = tf.placeholder(tf.float32, [None, 784])
        W1 = tf.Variable(tf.random_normal_initializer()([784, 100]))
        b1 = tf.Variable(tf.random_normal_initializer()([100]))
        W2 = tf.Variable(tf.random_normal_initializer()([100, 10]))
        b2 = tf.Variable(tf.random_normal_initializer()([10]))
        self.y = tf.matmul(tf.nn.relu(tf.matmul(x, W1) + b1), W2) + b2
        self.y_ = tf.placeholder(tf.float32, [None, 10])
        self.train_step = tf.train.MomentumOptimizer(0.1, 0.9).minimize(
          tf.reduce_mean(
              tf.nn.softmax_cross_entropy_with_logits(labels=self.y_, logits=self.y)))

class TestMethods(unittest.TestCase):
    def test0(self):
        m = NeonMNISTMLP()
        m.fit()
        self.assertAlmostEqual(0.97, m.accuracy(), 2)

    def test1(self):
        m = TensorFlowMNISTMLP()
        m.fit()
        self.assertAlmostEqual(0.97, m.accuracy(), 2)


if __name__ == "__main__":
    unittest.main()