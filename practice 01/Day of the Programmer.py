#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
def dayOfProgrammer(year):
    # For the transition year 1918
    if year == 1918:
        return "26.09.1918"
    
    # For Julian calendar years (1700 to 1917)
    if year < 1918:
        # Julian leap year if divisible by 4
        is_leap_year = (year % 4 == 0)
    else:
        # For Gregorian calendar years (1919 to 2700)
        # Gregorian leap year if divisible by 400 or divisible by 4 but not by 100
        is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    
    if is_leap_year:
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
