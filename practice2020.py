#-------------------------------------------------------------------------------
# Name:        practice2020.py
# Purpose:     Optimization problem
#
# Author:      Team Zeus
#
# Created:     February 2020
#
# N:B Create folders 'input' and 'output' where this script is placed
#-------------------------------------------------------------------------------

import os

workspace = os.path.dirname(os.path.realpath(__file__)).replace(os.sep, '/')

#---------------
#   FUNCTIONS
#---------------

# function to handle pizza sharing optimization
def optimization(maxPizza, pizzaData):

    maxPizza = 0

    currIndex, currValue, maxIndex, maxValue = [], [], [], [] # store current index and its value as well as index and value to give optimum maximum pizza

    pizzaSize = len(pizzaData) # full size of pizza

    while ( len(currIndex) > 0 ):

        start = pizzaSize - 1

        for i in range(start, -1, -1):
            currValue = pizzaData[i]
    
    return maxIndex

# function to handle file operations
def dataFiles(file):

    # input file name being examined
    print "++++++++++ FILE: " + file + " ++++++++++"

    # read input file
    input_file = open(file, 'r')
    
    # extract first and secondLine
    firstLine = input_file.readline()
    secondLine = input_file.readline()
    
    # close file
    input_file.close()

    # get maximum number of pizza slices to order,  number of different types of pizza and number of slices in each type of pizza
    maxPizza, typePizza = map(int, firstLine.split(" ")) # might need to wrap list() around for python3

    pizzaData = map(int, secondLine.split(" ")) # given in decreasing order # might need to wrap list() around for python3

    print maxPizza, typePizza, pizzaData

    print optimization(maxPizza, pizzaData)




#---------------
#     INPUTS
#---------------

input_files = ["a_example", "b_small"]
# input_files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

for i in range(len(input_files)):
    input_data = workspace + "/input/" + input_files[i] + ".in"
    dataFiles(input_data)



#---------------
#    OUTPUTS
#---------------
""" output_files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]

out_files = []
for i in range(len(output_files)):
    output_data = workspace + "/output/" + output_files[i] + ".out"
    out_files.append(output_data)
    f = open(output_data, "w+")
    # print f.readlines() """