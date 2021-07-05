import unittest

from src.cost_func import cost


# import

class CostFuncTest(unittest.TestCase):

    def test_cost_func(self):
        # given
        EXPECTED = 15
        # when
        ACTUAL = cost([1, 2, 3, 4, 5])
        # then
        self.assertEqual(EXPECTED, ACTUAL)
