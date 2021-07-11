"""
    Simulated annealing for the knapsack problem.
"""
import math
import random


# pylint: disable=R0913
# pylint: disable=too-many-arguments

class MySAProblem:
    """
        Class for the functions that solve the knapsack problem with SA.
    """

    def __init__(self, ksp):
        """
            Initialize parameters.
        """
        self.ksp = ksp
        self.state = self.generate_initial_state()

    def generate_initial_state(self):
        """
            Randomly generating the initial state of the elements in the knapsack.
        """
        state = []
        for _ in range(0, len(self.ksp.data)):
            state.append(random.randint(0, 1))
        return state

    def randomly_change_state(self):
        """
            Randomly generating the initial state of the elements in the knapsack.
        """
        changed_state = self.state
        index_of_changed_element = random.randint(0, 9)
        if (changed_state[index_of_changed_element]) == 0:
            changed_state[index_of_changed_element] = 1
        else:
            changed_state[index_of_changed_element] = 0
        return changed_state

    def solve(self):
        """
            Randomly generating the initial state of the elements in the knapsack.
        """

        current_temp = 200
        final_temp = .01
        alpha = 0.1
        # Start by initializing the current state
        # with the initial state, which is smaller than capacity
        while self.ksp.cost(self.state) > self.ksp.capacity:
            self.state = self.generate_initial_state()
        current_state = self.state

        while current_temp > final_temp:
            neighbor = self.randomly_change_state(current_state)
            cost_val_diff = self.ksp.calculate_value(current_state) - self.ksp.calculate_value(neighbor)

            if self.ksp.capacity >= self.ksp.cost(neighbor):
                if cost_val_diff < 0:
                    current_state = neighbor

                # if the new solution is not better,
                # accept it with a probability of e^(-cost/temp)
                else:
                    if random.uniform(0, 1) < math.exp(-cost_val_diff / current_temp):
                        current_state = neighbor

            # decrement the temperature
            current_temp -= alpha
        return current_state, self.ksp.cost(current_state)
