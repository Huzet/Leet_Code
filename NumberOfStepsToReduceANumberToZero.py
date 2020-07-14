#!/bin/python3

# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps (self, num: int) -> int:
        counter = 0
        placeholder = num
        while True:
            if placeholder == 0:
                return counter
            elif placeholder % 2 == 0:
                counter = counter + 1
                placeholder = placeholder / 2
                print(placeholder)
            elif placeholder % 2 == 1:
                counter = counter + 1
                placeholder = placeholder - 1
                print(placeholder)


# Details
# Runtime: 48 ms, faster than 13.01% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
# Memory Usage: 13.9 MB, less than 34.96% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.