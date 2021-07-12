"""
    Test for the simulated annealing.
"""

import unittest

from src.csv_read import read_csv_pandas
from src.knapsack_problem import KnapsackProblem
from src.simulated_annealing_kp_problem import MySAProblem


class CostFuncTest(unittest.TestCase):
    """
        The class that contains the test for the simulated annealing.
    """

    def test_cost_func(self):
        """
            The function to test the simulated annealing.
        """
        dataframe = read_csv_pandas("https://raw.githubusercontent.com/EKU-Summer-2021/"
                                    "intelligent_system_data/main/Intel"
                                    "ligent%20System%20Data"
                                    "/KP/KP_10.csv ")
        knapsack = KnapsackProblem(dataframe, 15)
        s_a = MySAProblem(knapsack)
        print(knapsack.data.columns)
        # given
        expected = ([0, 0, 0, 1, 1, 0, 0, 0, 0, 1], 15, 222)
        # when
        actual = s_a.solve()
        # then
        self.assertEqual(expected, actual)
