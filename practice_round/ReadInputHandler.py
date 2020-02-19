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

    def compare_feed(self, max_required, type_available, slices_in_pizza):
        pass
