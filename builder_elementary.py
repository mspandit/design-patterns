import unittest

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

class NeonMNISTMLP(object):
    def __init__(self, seed=None):
        super(NeonMNISTMLP, self).__init__()
        self.args = NeonArgparser().parse_args()
        self.dataset = MNIST(path=self.args.data_dir)
        gen_backend(rng_seed=seed, batch_size=self.args.batch_size)
        random.seed(seed)
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


import argparse
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

class TensorFlowMNISTMLP(object):
    def __init__(self, seed=None):
        super(TensorFlowMNISTMLP, self).__init__()
        if seed:
            tf.set_random_seed(seed)
        parser = argparse.ArgumentParser()
        parser.add_argument('--data_dir', type=str, default='/tmp/mnist_data', 
                            help='Directory for storing input data')
        self.FLAGS, self.unparsed = parser.parse_known_args()
        self.dataset = input_data.read_data_sets(self.FLAGS.data_dir, 
                                                 one_hot=True)
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
        self.sess = tf.InteractiveSession()
        tf.global_variables_initializer().run()
              
    def fit(self):
        for _ in range(4690):
            batch_xs, batch_ys = self.dataset.train.next_batch(128)
            self.sess.run(self.train_step, 
                          feed_dict={self.x: batch_xs, self.y_: batch_ys})

    def accuracy(self):
        return self.sess.run(self.acc, feed_dict={
                self.x: self.dataset.test.images, 
                self.y_: self.dataset.test.labels
        })


class TestMethods(unittest.TestCase):
    def test0(self):
        m = NeonMNISTMLP(1)
        m.fit()
        self.assertAlmostEqual(0.9746, m.accuracy(), 4)

    def test1(self):
        m = TensorFlowMNISTMLP(1)
        m.fit()
        self.assertAlmostEqual(0.9275, m.accuracy(), 4)


if __name__ == "__main__":
    unittest.main()