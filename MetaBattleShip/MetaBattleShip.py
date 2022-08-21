#!/usr/bin/env python3


import sys
import math
from typing import List

class Solution(object):
    def __init__(self):
        pass
    def countBattleships(self) -> int:
        board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
        m = len(board)
        n = len(board[0])
        count = 0

        for i in range(m):
            for j in range(n):
                print("i:",i,"j:",j,"board[i][j]",board[i][j],count)
                if (board[i][j] == '.'):
                    print(".")
                    continue
                if (i>0 and board[i-1][j] == 'X'):
                    print("i")
                    continue
                if (j>0 and board[i][j-1] == 'X'):
                    print("j")
                    continue
                count+=1
                print("i:",i,"j:",j,"board[i][j]",board[i][j],count)
        return count