# -------------------------------------------------------------------------------
# Name:        OptimizationHandler.py
# Purpose:     Optimization problem
#
# Author:      Team Zeus
#
# Created:     February 2020
#
# -------------------------------------------------------------------------------


from handlers.ReadInputHandler import ReadInputHandler
from handlers.WriteOutputHandler import WriteOutputHandler


class OptimizationHandler(ReadInputHandler):
    def __init__(self, input_file, output_file):

        super().__init__(input_file)

        output = self.solve()

        if output != None:
            WriteOutputHandler(output_file, output)

    def solve(self):
        if self.pizza_type_slices[-1] > self.pizza_slice_max:
            return None

        step = 0
        all_combinations = []
        deficit = []

        for i in range((self.pizza_types - 1), -1, -1):
            pizza_needed = self.pizza_slice_max
            order_pizza = []

            for j in range(((self.pizza_types - 1) - step), -1, -1):
                if pizza_needed - self.pizza_type_slices[j] >= 0:
                    order_pizza.append(j)
                    pizza_needed -= self.pizza_type_slices[j]

            deficit.append(pizza_needed)
            all_combinations.append(order_pizza)
            step += 1

        optimized = deficit.index(min(deficit))

        optimized = all_combinations[optimized]
        optimized.reverse()

        print(
            f"\nPizza slice deficit for {self.filname} is: {min(deficit)}")

        return (len(optimized), optimized)
