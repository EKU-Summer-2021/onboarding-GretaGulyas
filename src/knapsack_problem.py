"""
    Knapsack problem solver on calculating the cost of the knapsack.
"""


# pylint: disable=too-few-public-methods

class KnapsackProblem:
    """
        The class that contains the cost func.
    """

    def __init__(self, dataframe, capacity):
        self.data = dataframe
        self.capacity = capacity

    def cost(self, items):
        """
            The cost func itself.
        """

        knapsack_cost = 0
        for index, item in enumerate(items):
            if item == 1:
                knapsack_cost += self.data.weight[index]
        return knapsack_cost
