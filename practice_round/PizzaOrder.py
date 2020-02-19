# -------------------------------------------------------------------------------
# Name:        PizzaOrder.py
# Purpose:     Optimization problem
#
# Author:      Team Zeus
#
# Created:     February 2020
#
# N:B Create folders 'input' and 'output' where this script is placed
# -------------------------------------------------------------------------------


import os
from threading import Thread

from ReadInputHandler import ReadInputHandler
from WriteOutputHandler import WriteOutputHandler


class PizzaOrder:
    def __init__(self, input_file=None, output_file=None):
        if not os.path.isdir("output"):
            os.mkdir("output")

        pih = ReadInputHandler(input_file)
        output = pih.solve()

        # if output != None:
        #     woh = WriteOutputHandler(output_file, output)


if __name__ == "__main__":
    # input_files = ["a_example", "b_small",
    #                "c_medium", "d_quite_big", "e_also_big"]

    input_files = ["b_small"]

    thread_list = []

    for i in range(len(input_files)):
        # thread = Thread(target=PizzaOrder, args=(f"input/{input_files[i]}.in",
        #                                          f"output/{input_files[i]}.out"))
        # thread_list.append(thread)
        # thread.start()

        # for thread in thread_list:
        #     thread.join()

        PizzaOrder(f"input/{input_files[i]}.in",
                   f"output/{input_files[i]}.out")
