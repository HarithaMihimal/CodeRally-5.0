#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    max_spent = -1  # Initialize the maximum amount spent to -1 (in case no valid combination is found)
    
    # Iterate over each keyboard price
    for keyboard in keyboards:
        # Iterate over each drive price
        for drive in drives:
            total_cost = keyboard + drive  # Calculate the total cost of this combination
            # Check if this total cost is within the budget and if it's the highest we've found so far
            if total_cost <= b and total_cost > max_spent:
                max_spent = total_cost  # Update the maximum amount spent
    
    return max_spent


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
