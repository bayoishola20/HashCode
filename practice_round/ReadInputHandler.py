# -------------------------------------------------------------------------------
# Name:        ReadInputHandler.py
# Purpose:     Optimization problem
#
# Author:      Team Zeus
#
# Created:     February 2020
#
# -------------------------------------------------------------------------------

from pathlib import Path


class ReadInputHandler:
    def __init__(self, filename):
        self.filname = filename
        if self.filname != None:
            print(
                f"\n++++++++ Reading input from FILE:  {self.filname} ++++++++")

            with open(self.filname, "r") as f:
                data = f.readlines()
                data = [d.strip() for d in data]

                self.pizza_slice_max, self.pizza_types = map(
                    int, data[0].split(" "))
                self.pizza_type_slices = list(map(int, data[1].split(" ")))

    def solve(self):
        if self.pizza_type_slices[-1] > self.pizza_slice_max:
            return None

        pizza_varieties, pizza_type, deficit = self.calculate(
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, 1, 1)

        print(
            f"\nPizza slice deficit for {self.filname} is: {deficit}")

        return (pizza_varieties, pizza_type)

    def calculate(self, max_required, types_available, slices_in_pizza, direction, step):

        kernel = 0
        all_combinations = []
        deficit = []
        optimized = None

        if direction == -1:
            length_types = types_available - 1
        else:
            length_types = types_available

        print(length_types, direction, step)

        for i in range(length_types, direction, step):
            pizza_needed = max_required
            print(pizza_needed)
            order_pizza = []

            for j in range((length_types - kernel), direction, step):
                if pizza_needed - slices_in_pizza[j] >= 0:
                    order_pizza.append(j)
                    pizza_needed -= slices_in_pizza[j]

            print(pizza_needed)

            deficit.append(pizza_needed)
            all_combinations.append(order_pizza)

            kernel += 1

        # optimized = deficit.index(min(deficit))
        # optimized = all_combinations[optimized]

        # optimized.reverse()

        return (1, 2, 1)

        # return (len(optimized), optimized, min(deficit))
