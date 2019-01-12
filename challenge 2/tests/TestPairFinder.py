import unittest
import collections
from PairFinder import PairFinder


class TestPairFinder(unittest.TestCase):

    def setUp(self):
        self.Item = collections.namedtuple('Item', ['name', 'price'])
        self.Item0 = self.Item(name='Candy Bar', price=500)
        self.Item1 = self.Item(name='Paperback Book', price=700)
        self.Item2 = self.Item(name='Detergent', price=1000)
        self.Item3 = self.Item(name='Headphones', price=1400)
        self.Item4 = self.Item(name='Earmuffs', price=2000)
        self.Item5 = self.Item(name='Bluetooth Steroe', price=6000)
        self.items = [self.Item0, self.Item1, self.Item2, self.Item3, self.Item4, self.Item5]
        self.pf = PairFinder(self.items)

    # Tests for algorithm with runtime O(n)
    def test_find_in_O_n(self):
        max_price = 1500
        pair = self.pf.find_in_O_n(max_price)
        exp = [self.Item0, self.Item2]
        self.assertEqual(exp, pair)

    def test_find_in_O_n_too_small(self):
        max_price = 100
        pair = self.pf.find_in_O_n(max_price)
        exp = [None, None]
        self.assertEqual(exp, pair)

    def test_find_in_O_n_too_big(self):
        max_price = 10000
        pair = self.pf.find_in_O_n(max_price)
        exp = [self.Item4, self.Item5]
        self.assertEqual(exp, pair)

    def test_find_in_O_n_cross(self):
        max_price = 2450
        pair = self.pf.find_in_O_n(max_price)
        exp = [self.Item2, self.Item3]
        self.assertEqual(exp, pair)

    # Tests for algorithm with runtime O(n^2)
    def test_find_in_O_n2(self):
        max_price = 1500
        pair = self.pf.find_in_O_n2(max_price)
        exp = [self.Item0, self.Item2]
        self.assertEqual(exp, pair)

    def test_find_in_O_n2_too_small(self):
        max_price = 100
        pair = self.pf.find_in_O_n2(max_price)
        exp = [None, None]
        self.assertEqual(exp, pair)

    def test_find_in_O_n2_too_big(self):
        max_price = 10000
        pair = self.pf.find_in_O_n2(max_price)
        exp = [self.Item4, self.Item5]
        self.assertEqual(exp, pair)


if __name__ == '__main__':
    unittest.main()
