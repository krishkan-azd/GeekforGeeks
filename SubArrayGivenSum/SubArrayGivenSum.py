#!/usr/bin/env python3
''' Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

In case of multiple subarrays, return the subarray which comes first on moving from left to right.

 

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
 

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15. 

For this, consider each subarray as a Sliding Window of size ‘k’. To calculate the sum of the next subarray, we need to slide the window ahead by one element. So to slide the window forward and calculate the sum of the new position of the sliding window, we need to do two things:
	1. Subtract the element going out of the sliding window i.e., subtract the first element of the window.
	2. Add the new element getting included in the sliding window i.e., the element coming right after the end of the window.
This approach will save us from re-calculating the sum of the overlapping part of the sliding window. Here is what our algorithm will look like:

From <https://www.educative.io/collection/page/5668639101419520/5671464854355968/5177043027230720> 
'''

import sys

class Solution(object):
	def __init__(self):
		pass
	def subArraySum(arr,n,s):
		arrli=[]
		win_sum,win_start,win_end=0,0,0
		for win_end in range(len(arr)):
			win_sum+=arr[win_end] # add the next element
			print("win_start is:",win_start,"win_end is:",win_end,"win_sum is:",win_sum, "array is:", arr, "max_sum_arr_len:", n,"Max Sum:", s)
			while(win_sum > s):
				print("win_start is:",win_start,"win_end is:",win_end,"win_sum is:",win_sum, "array is:", arr)
				win_sum = win_sum - arr[win_start]
				win_start += 1
			if (win_sum == s):
				print("win_start is:",win_start,"win_end is:",win_end,"win_sum is:",win_sum, "array is:", arr)
				break
			win_end +=1 
		if(win_end<n and win_start <= win_end):
			arrli.append(win_start+1)
			arrli.append(win_end+1)
		else:
			arrli.appen(-1)		
			
		return arrli

	

