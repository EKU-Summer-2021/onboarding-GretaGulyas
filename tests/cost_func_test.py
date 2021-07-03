import unittest

from src.cost_func import cost


class CostFuncTest(unittest.TestCase):

    def test_cost_func(self):
        # given
        EXPECTED = 10
        # when
        ACTUAL = cost(5, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
        # then
        self.assertEqual(EXPECTED, ACTUAL)
