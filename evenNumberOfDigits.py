#!/bin/python3

# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/submissions/

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for place in nums:
            if (len(str(place)) % 2) == 0:
                counter = counter + 1
        return counter

# Success
# Details
# Runtime: 52 ms, faster than 86.66% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 37.85% of Python3 online submissions for Find Numbers with Even Number of Digits.