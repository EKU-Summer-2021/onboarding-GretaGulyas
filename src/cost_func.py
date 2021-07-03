"""
    Knapsack problem solver on calculating the cost of the knapsack.
"""


# Given a set of items, each with a mass and a value, determine the number of each item
# to include in a collection so that the total weight is less than or equal to a given
# limit and the total value is as large as possible.


class CostOfKnapsack:
    """
        The class that contains the cost func.
    """


def cost(total_capacity, values, weights):
    """
        The cost func itself, which returns the cost of a configuration of items in the knapsack.
    """

    if total_capacity == 0:
        return 0
    # If the capacity is 0, the knapsack cannot be loaded.

    loaded_capacity = 0
    total_cost = 0

    for i in weights:
        while loaded_capacity <= total_capacity:
            for j in weights:
                loaded_capacity += weights[i]
                total_cost += values[i]
        return total_cost
