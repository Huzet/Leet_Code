#! Python3

# https://leetcode.com/problems/decompress-run-length-encoded-list/

nums = [1,1,2,3]
# Output: [1,3,3]

def decompressRLElist(nums):
    newlist = []
    for x in range(0, len(nums), 2):
        counter = nums[x] 
        print(counter)
        while counter != 0:
            newlist.append(nums[x+1])
            counter = counter - 1
    return newlist
        

decompressRLElist(nums)

"""Results below"""
# Success
# Details
# Runtime: 80 ms, faster than 42.66% of Python3 online submissions for Decompress Run-Length Encoded List.
# Memory Usage: 13.7 MB, less than 99.84% of Python3 online submissions for Decompress Run-Length Encoded List.