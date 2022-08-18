#!/usr/bin/env python3


import sys
import math
from typing import List

class Solution(object):
    def __init__(self):
        pass
    def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
        current=1
        result=0
        #print("N:",N,"M:",M,"C:",C)
        for i in range(M):
            #print("i:",i,"current:",current,"C[i]:",C[i],"result:",result)
            toPick = C[i]
            if(toPick == current):
                continue
            timeLeft = (N+current-toPick)%N
            timeRight= (N-current+toPick)%N

            result+= min(timeLeft,timeRight)
            current = toPick

            #print("i:",i,"current:",current,"toPick:",toPick,"C[i]:",C[i],"timeLeft:",timeLeft,"timeRight:",timeRight,"result:",result)
        return result