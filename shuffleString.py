#! Python3

# https://leetcode.com/problems/shuffle-string/


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answerList = ['']*len(s)
        sList = [s[i:i+1] for i in range(0, len(s))]
        for x in range(0, len(indices)):
            answerList[indices[x]] = sList[x] 
        return (''.join(answerList))

"""Results below"""
# Success
# Details
# Runtime: 72 ms, faster than 53.26% of Python3 online submissions for Shuffle String.
# Memory Usage: 13.8 MB, less than 52.32% of Python3 online submissions for Shuffle String.
# Next challenges: 
