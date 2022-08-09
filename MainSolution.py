#!/usr/bin/env python3


import sys
from SubArrayGivenSum import Solution

def main():
    ''' ./MainSolution.py array, n_size_array_for_sum , sum
    python .MainSolution.py
win_start is: 0 win_end is: 0 win_sum is: 1 array is: [1, 2, 3, 7, 5] max_sum_arr_len: 5 Max Sum: 12
win_start is: 0 win_end is: 1 win_sum is: 3 array is: [1, 2, 3, 7, 5] max_sum_arr_len: 5 Max Sum: 12
win_start is: 0 win_end is: 2 win_sum is: 6 array is: [1, 2, 3, 7, 5] max_sum_arr_len: 5 Max Sum: 12
win_start is: 0 win_end is: 3 win_sum is: 13 array is: [1, 2, 3, 7, 5] max_sum_arr_len: 5 Max Sum: 12
win_start is: 0 win_end is: 3 win_sum is: 13 array is: [1, 2, 3, 7, 5]
win_start is: 1 win_end is: 3 win_sum is: 12 array is: [1, 2, 3, 7, 5]
[2, 4]
python .MainSolution.py
win_start is: 0 win_end is: 0 win_sum is: 1 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] max_sum_arr_len: 10 Max Sum: 15
win_start is: 0 win_end is: 1 win_sum is: 3 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] max_sum_arr_len: 10 Max Sum: 15
win_start is: 0 win_end is: 2 win_sum is: 6 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] max_sum_arr_len: 10 Max Sum: 15
win_start is: 0 win_end is: 3 win_sum is: 10 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] max_sum_arr_len: 10 Max Sum: 15
win_start is: 0 win_end is: 4 win_sum is: 15 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] max_sum_arr_len: 10 Max Sum: 15
win_start is: 0 win_end is: 4 win_sum is: 15 array is: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[1, 5]

    '''
    arr = [1,2,3,4,5,6,7,8,9,10]
    n=10
    s=15
    SubArrayIndicies = Solution.subArraySum(arr,n,s)
    print(SubArrayIndicies)

if __name__ == '__main__':
    main()