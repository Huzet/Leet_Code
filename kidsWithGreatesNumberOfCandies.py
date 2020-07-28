#! Python3

# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

candies = [2,3,5,1,3]
extraCandies = 3
# [true,true,true,false,true] 
# candies = [4,2,1,1,2]
# extraCandies = 1
# [true,false,false,false,false] 

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        newlist = []
        for candy in candies:
            if max(candies) <= candy + extraCandies:
                newlist.append(True)
            else:
                newlist.append(False)
        return newlist


# Success
# Details
# Runtime: 28 ms, faster than 98.89% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Memory Usage: 14 MB, less than 22.65% of Python3 online submissions for Kids With the Greatest Number of Candies.
# Next challenges: 