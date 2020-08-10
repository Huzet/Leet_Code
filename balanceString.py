#! Python3

s = "RLLLLRRRLR"
# Output: 4
# Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

def balancedStringSplit(s):
    R = 0
    L = 0
    counter = 0
    for letter in s:
        if letter == 'R':
            R = R + 1
            if L == R:
                counter = counter + 1
                R = 0
                L = 0
        elif letter == 'L':
            L = L + 1
            if L == R:
                counter = counter + 1
                R = 0
                L = 0
    return counter

# Success
# Details
# Runtime: 16 ms, faster than 99.93% of Python3 online submissions for Split a String in Balanced Strings.
# Memory Usage: 14 MB, less than 21.07% of Python3 online submissions for Split a String in Balanced Strings.