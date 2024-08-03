#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def climbingLeaderboard(ranked, player):
    # Remove duplicates and sort in descending order
    unique_ranked = sorted(set(ranked), reverse=True)
    player_ranks = []
    l = len(unique_ranked)
    index = l - 1  # Start from the end of the unique ranked list
    
    for score in player:
        while index >= 0 and score >= unique_ranked[index]:
            index -= 1
        player_ranks.append(index + 2)  # Rank is index + 2 because index + 1 is the number of scores above the player
        
    return player_ranks

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
