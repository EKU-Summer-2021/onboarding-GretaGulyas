"""
    Knapsack problem test.
"""

import unittest

import numpy as np

from src.csv_read import read_csv_pandas
from src.knapsack_problem import KnapsackProblem


class CostFuncTest(unittest.TestCase):

    def test_cost_func(self):
        dataframe = read_csv_pandas("https://raw.githubusercontent.com/EKU-Summer-2021/"
                                    "intelligent_system_data/main/Intel"
                                    "ligent%20System%20Data"
                                    "/KP/KP_10.csv ")
        knapsack = KnapsackProblem(dataframe)
        # given
        expected = 41
        # when
        actual = knapsack.cost(np.array([0, 1, 0, 1, 1, 0, 1, 0]))
        # then
        self.assertEqual(expected, actual)
