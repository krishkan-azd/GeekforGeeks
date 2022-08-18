#!/usr/bin/env python3


import sys
import math
from typing import List

class Solution(object):
    def __init__(self):
        pass
    def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
        eaten = 0
        history = {}
        for i in range(N):
            k = history.get(D[i])
            if(k==None or (eaten-k)>K):
                history[D[i]]=eaten
                eaten+=1
                #print("k:",k,"history:",history,"eaten:",eaten)
        return eaten