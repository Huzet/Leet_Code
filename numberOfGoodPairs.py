#!/bin/python3

# https://leetcode.com/problems/number-of-good-pairs/submissions/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for x in range(0, len(nums)):
            for y in range((x+1), len(nums)):
                if nums[x] == nums[y] :
                    count = count + 1
                else:
                    pass
        return count

# Success
# Details
# Runtime: 40 ms, faster than 66.67% of Python3 online submissions for Number of Good Pairs.
# Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Number of Good Pairs.
# Next challenges: 