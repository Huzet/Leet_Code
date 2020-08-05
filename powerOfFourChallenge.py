#! Python 3

# https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/549/week-1-august-1st-august-7th/3412/

num = 16
# Output: true

# num = 5
# Output: false

# num = -2147483648
# Output: false

def isPowerOfFour(num):
    if num == 0:
        return False
    while num !=1:
        if num % 4 !=0:
            return False
        num = num // 4

    return True

# 1060 / 1060 test cases passed.
# Status: Accepted
# Runtime: 32 ms
# Memory Usage: 13.5 MB

x = isPowerOfFour(num)
print(16 // 4)   
print(num % 4 !=0)