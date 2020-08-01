#! Python3

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        greaterThan = []
        counter = 0
        for num in nums:
            for Cnum in nums:
                if num > Cnum:
                    counter = counter + 1
            greaterThan.append(counter)
            counter = 0
        return greaterThan

# Success
# Details
# Runtime: 292 ms, faster than 42.46% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.1 MB, less than 11.27% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.

smallerNumbersThanCurrent(nums)