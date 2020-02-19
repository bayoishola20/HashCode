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
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, "forward", "backward")

        backward_backward = self.calculate(
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, "backward", "backward")

        backward_forward = self.calculate(
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, "backward", "forward")

        forward_backward = self.calculate(
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, "forward", "backward")

        forward_forward = self.calculate(
            self.pizza_slice_max, self.pizza_types, self.pizza_type_slices, "forward", "forward")

        results = [backward_backward[2], backward_forward[2],
                   forward_backward[2], forward_forward[2]]

        print(results)

        print(
            f"\nPizza slice deficit for {self.filname} is: {deficit}")

        return (pizza_varieties, pizza_type)

    def calculate(self, max_required, types_available, slices_in_pizza, direction, window):

        kernel = 0
        all_combinations = []
        deficit = []
        optimized = None

        if direction == "backward":
            if window == "backward":
                for i in range(types_available - 1, -1, -1):
                    pizza_needed = max_required
                    order_pizza = []

                    for j in range((types_available - 1 - kernel), -1, -1):
                        if pizza_needed - slices_in_pizza[j] >= 0:
                            order_pizza.append(j)
                            pizza_needed -= slices_in_pizza[j]

                    deficit.append(pizza_needed)
                    all_combinations.append(order_pizza)
                    kernel += 1

            else:
                for i in range(types_available - 1, -1, -1):
                    pizza_needed = max_required
                    order_pizza = []

                    for j in range((types_available - kernel)):
                        if pizza_needed - slices_in_pizza[j] >= 0:
                            order_pizza.append(j)
                            pizza_needed -= slices_in_pizza[j]

                    deficit.append(pizza_needed)
                    all_combinations.append(order_pizza)
                    kernel += 1
        else:
            if window == "backward":
                for i in range(types_available):
                    pizza_needed = max_required
                    order_pizza = []

                    for j in range((types_available - 1 - kernel), -1, -1):
                        if pizza_needed - slices_in_pizza[j] >= 0:
                            order_pizza.append(j)
                            pizza_needed -= slices_in_pizza[j]

                    deficit.append(pizza_needed)
                    all_combinations.append(order_pizza)
                    kernel += 1

            else:
                for i in range(types_available):
                    pizza_needed = max_required
                    order_pizza = []

                    for j in range((types_available - kernel)):
                        if pizza_needed - slices_in_pizza[j] >= 0:
                            order_pizza.append(j)
                            pizza_needed -= slices_in_pizza[j]

                    deficit.append(pizza_needed)
                    all_combinations.append(order_pizza)
                    kernel += 1

        optimized = deficit.index(min(deficit))
        optimized = all_combinations[optimized]

        optimized.reverse()

        # return (1, 2, 1)

        return (len(optimized), optimized, min(deficit))
