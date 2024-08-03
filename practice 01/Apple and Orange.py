#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculate the landing positions of apples
    apples_land = [a + apple for apple in apples]
    # Calculate the landing positions of oranges
    oranges_land = [b + orange for orange in oranges]
    
    # Count apples that land on the house
    apples_on_house = sum(1 for apple in apples_land if s <= apple <= t)
    
    # Count oranges that land on the house
    oranges_on_house = sum(1 for orange in oranges_land if s <= orange <= t)
    
    # Print the counts
    print(apples_on_house)
    print(oranges_on_house)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
