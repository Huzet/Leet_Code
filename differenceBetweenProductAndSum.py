#! Python3

# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Nlist= [int(char) for char in str(n)]
        productNum = 1
        for num in Nlist:
            productNum = productNum * num 
        return (productNum - sum(Nlist))

# Success
# Details
# Runtime: 28 ms, faster than 81.38% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.9 MB, less than 36.20% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.