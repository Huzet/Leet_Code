#!/bin/python3

# https://leetcode.com/problems/xor-operation-in-an-array/

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        rounds = 0    
        while rounds < n:
            nums.append(start + 2*rounds)
            rounds = rounds + 1
        
        answer = nums[0]
        for x in range(1,n):
            answer = answer ^ nums[x]
        return answer

"""Results below"""
# Success
# Details
# Runtime: 56 ms, faster than 11.23% of Python3 online submissions for XOR Operation in an Array.
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for XOR Operation in an Array.