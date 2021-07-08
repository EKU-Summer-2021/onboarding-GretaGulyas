"""
    Knapsack problem test.
"""

import unittest

import numpy as np

from src.csv_read import read_csv_pandas
from src.knapsack_problem import KnapsackProblem


# test

class CostFuncTest(unittest.TestCase):
    """
        The class that contains the test for the cost function.
    """

    def test_cost_func(self):
        """
            The function to test the cost().
        """
        dataframe = read_csv_pandas("https://raw.githubusercontent.com/EKU-Summer-2021/"
                                    "intelligent_system_data/main/Intel"
                                    "ligent%20System%20Data"
                                    "/KP/KP_10.csv ")
        knapsack = KnapsackProblem(dataframe, 15)
        # given
        expected = 41
        # when
        actual = knapsack.cost(np.array([0, 1, 0, 1, 1, 0, 1, 0]))
        # then
        self.assertEqual(expected, actual)
