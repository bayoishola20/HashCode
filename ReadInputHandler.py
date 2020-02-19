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
import numpy as np


class ReadInputHandler:
    def __init__(self, filename):
        if filename != None:
            print(f"\n++++++++ Reading input from FILE:  {filename} ++++++++")

            with open(filename, "r") as f:
                data = f.readlines()
                data = [d.strip() for d in data]

                self.pizza_slice_max, self.pizza_types = map(
                    int, data[0].split(" "))
                self.pizza_type_slices = list(map(int, data[1].split(" ")))

    def solve(self):
        if self.pizza_type_slices[-1] > self.pizza_slice_max:
            return None

        order_pizza = []

        for i in range((self.pizza_types - 1), -1, -1):

            if self.pizza_slice_max - self.pizza_type_slices[i] > 0:
                order_pizza.append(i)
                self.pizza_slice_max -= self.pizza_type_slices[i]

        order_pizza.reverse()

        return (len(order_pizza), order_pizza)
