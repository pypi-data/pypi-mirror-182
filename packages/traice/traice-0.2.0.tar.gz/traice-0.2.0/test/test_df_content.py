from unittest import TestCase

from random import uniform, seed
from time import sleep, time

from traice import Traicer


def train_step():
    sleep(uniform(0, 1))


class TestDfContent(TestCase):

    def setUp(self):
        traicer = Traicer()

        seed(17)

        init_timestamp = time()

        for i in range(1, 5):
            start_timestamp = time()
            train_step()
            traicer.push(i, uniform(0, 1 / i), (time_ := time()) - start_timestamp, time_ - init_timestamp)

        self.traicer = traicer

    def test_n_rows(self):
        self.assertEqual(len(self.traicer.df.index), 4)

    def test_mean_loss(self):
        self.assertAlmostEqual(self.traicer.df['loss'].mean(), 0.30344598346)
