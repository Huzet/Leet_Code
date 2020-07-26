#!/bin/python3

# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        backarr = nums[:n]
        frontarr = nums[n:]
        nums = []
        for x in range(n):
            nums.append(backarr[x])
            nums.append(frontarr[x])
        return nums

# Success
# Details
# Runtime: 52 ms, faster than 99.18% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Shuffle the Array.
