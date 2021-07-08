"""
    Simulated annealing for the knapsack problem.
"""
import math
import random


class MySAProblem:
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
        for i in range(0, len(self.ksp.data)):
            state.append(random.randint(0, 1))
        return state

    # todo snake_case
    def randomly_change_state(self):
        """
            Randomly generating the initial state of the elements in the knapsack.
        """
        changed_state = self.state
        IndexOfChangedElement = random.randint(0, 9)
        if (changed_state[IndexOfChangedElement]) == 0:
            changed_state[IndexOfChangedElement] = 1
        else:
            changed_state[IndexOfChangedElement] = 0
        return changed_state

    def solve(self):
        """
            Randomly generating the initial state of the elements in the knapsack.
        """
        initial_temp = 90
        final_temp = .1
        alpha = 0.01

        current_temp = initial_temp

        # Start by initializing the current state with the initial state
        current_state = self.state
        print(current_state)
        solution = current_state

        while current_temp > final_temp:
            neighbor = self.randomly_change_state()
            # Check if neighbor is best so far
            print("Current state", current_state)
            print("Neighbor", neighbor)
            cost_diff = self.ksp.cost(current_state) - self.ksp.cost(neighbor)

            # if the new solution is better, accept it
            if cost_diff > 0:
                solution = neighbor
            # if the new solution is not better, accept it with a probability of e^(-cost/temp)
            else:
                if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                    solution = neighbor
            # decrement the temperature
            current_temp -= alpha

        return solution
