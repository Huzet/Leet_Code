#!/bin/python3

# https://leetcode.com/problems/defanging-an-ip-address/submissions/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')


"""Results below"""
# Success
# Details
# Runtime: 40 ms, faster than 19.76% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 13.8 MB, less than 51.19% of Python3 online submissions for Defanging an IP Address.