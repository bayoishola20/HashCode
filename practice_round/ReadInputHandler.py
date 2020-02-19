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
    # handles file inputs and reading of input data
    def __init__(self, filename):
        self.filname = filename

        # check if input file exists then proceed
        if self.filname != None:
            print(
                f"\n++++++++ Reading input from FILE:  {self.filname} ++++++++")

            # read input file
            with open(self.filname, "r") as f:
                data = f.readlines() # read all lines
                data = [d.strip() for d in data]

                # get maximum number of pizza slices to order and number of different types of pizza
                self.pizza_slice_max, self.pizza_types = map(
                    int, data[0].split(" "))

                # number of slices in each type of pizza
                self.pizza_type_slices = list(map(int, data[1].split(" ")))
            
            f.close() # added close

    def solve(self):
        # if last item in the pizza slices is greater than max slices to get, return None
        if self.pizza_type_slices[-1] > self.pizza_slice_max:
            return None

        step = 0
        all_combinations = [] # possible pizza slices combination to get max number of pizza slices
        deficit = [] # what is left after finding a possible max combination

        # looping through the range of pizza types which also represents the slices on line 2 of input file, we go from the last item and one step 
        for i in range((self.pizza_types - 1), -1, -1):
            # pizza needed at the end of the day
            pizza_needed = self.pizza_slice_max
            order_pizza = [] # array of pizza to be ordered

            for j in range(((self.pizza_types - 1) - step), -1, -1):
                # check if difference in pizza_needed (same as pizza_slice_max) and value of number of slices to check from is greater than or equal to zero, then append to the array of pizzas to order (order_pizza). Repeat difference!
                if pizza_needed - self.pizza_type_slices[j] >= 0:
                    order_pizza.append(j)
                    pizza_needed -= self.pizza_type_slices[j]
            

            deficit.append(pizza_needed)
            all_combinations.append(order_pizza)
            step += 1 # increase step

        optimized = deficit.index(min(deficit))

        optimized = all_combinations[optimized]
        optimized.reverse()

        print(
            f"\nPizza slice deficit for {self.filname} is: {min(deficit)}")

        return (len(optimized), optimized)
