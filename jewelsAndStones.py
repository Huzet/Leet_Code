#! python3

# https://leetcode.com/problems/jewels-and-stones/


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Jlist= [char for char in J] 
        Slist= [char for char in S] 
        count = 0
        for letter in Jlist:
            count = Slist.count(letter) + count
        return count


# Success
# Details
# Runtime: 28 ms, faster than 84.55% of Python3 online submissions for Jewels and Stones.
# Memory Usage: 13.7 MB, less than 91.20% of Python3 online submissions for Jewels and Stones.
# Next challenges: 