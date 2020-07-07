#!/bin/python3

# https://leetcode.com/problems/running-sum-of-1d-array/



class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_arr = []
        for x in range(0, len(nums)):
            placeholder = nums[x]
            for y in range(0,x):
                placeholder = nums[y] + placeholder 
            new_arr.append(placeholder)
        return new_arr

"""Results below"""
# Success
# Details
# Runtime: 172 ms, faster than 5.02% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.1 MB, less than 33.33% of Python3 online submissions for Running Sum of 1d Array.