#!/bin/python3

# https://leetcode.com/problems/roman-to-integer/

# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        romanInt = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000,
                    }
        placeH = 0  
        convertedValue = 0          
        while placeH < len(s):
            if (placeH + 1) < len(s) and romanInt[s[placeH]] >= romanInt[s[placeH + 1]]:
                convertedValue = convertedValue + romanInt[s[placeH]]
                placeH = placeH + 1
            elif (placeH + 1) < len(s) and romanInt[s[placeH]] < romanInt[s[placeH + 1]]:
                convertedValue = convertedValue + (romanInt[s[placeH + 1]] - romanInt[s[placeH]])
                placeH = placeH + 2
            elif (placeH + 1) == len(s):
                convertedValue = convertedValue + romanInt[s[placeH]]
                placeH = placeH + 1
        return convertedValue
 
# Success
# Details
# Runtime: 88 ms, faster than 6.27% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.7 MB, less than 92.57% of Python3 online submissions for Roman to Integer.