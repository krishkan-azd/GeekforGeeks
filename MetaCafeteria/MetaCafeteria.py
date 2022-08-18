#!/usr/bin/env python3


import sys
import math
from typing import List

class Solution(object):
    def __init__(self):
        pass
    def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
        start = 1
        availableSeats = 0
        S.append(-K)        
        S.append(N+K+1)
        S.sort()
        print("S:",S)
        ''' for diner in S:
            delta = diner - K - start
            print(diner, delta, K ,start)
            if delta > 0:
                availableSeats += math.ceil(delta/(K+1))
            start = diner+K+1
            return availableSeats
        '''

        #get ranges of free seats
        ranges = [S[i+1]-S[i] for i in range(len(S)-1)]
        print("ranges:",ranges)

        #get max # of seats that can be taken in each range
        max_seats = [int(x/(K+1)-1) for x in ranges]
        print("MaxSeats:",max_seats)
        return sum(max_seats)