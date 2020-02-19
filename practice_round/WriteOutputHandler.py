# -------------------------------------------------------------------------------
# Name:        WriteOutputHandler.py
# Purpose:     Optimization problem
#
# Author:      Team Zeus
#
# Created:     February 2020
#
# -------------------------------------------------------------------------------

from pathlib import Path


class WriteOutputHandler:
    def __init__(self, filename, output):
        # validate filename and output isn't None
        if filename != None and output != None:
            print(f"\n++++++++ Writing output to FILE: {filename} ++++++++")
            # write into output file
            with open(filename, "w+") as f:
                f.write(f"{output[0]}\n")

                # index output
                for i, pizza in enumerate(output[1]):
                    if i < len(output[1]) - 1:
                        f.write(f"{pizza} ")
                    else:
                        f.write(f"{pizza}\n")

            f.close()
