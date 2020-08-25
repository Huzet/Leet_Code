#! Python3

# https://leetcode.com/problems/sort-the-matrix-diagonally/

import re

# Input: 
mat = [ [3,3,1,1],
        [2,2,1,2],
        [1,1,1,2] ]

compare = [3,2,1,3,1,2,1,2,1,2,1,1]

# 1. Seperate diagonaly
# 2. Group in diagonal groups
# [[3,2,1],     3
# [3,1,2],      3
# [1,2],        2
# [1],          1
# [2,1],        2
# [1]]          1
# 
# 4 X 3 
# 

# Output: [ [1,1,1,1],  00 01 02 03 XX    1
#           [1,2,2,2],  10 11 12 13 XX    21       
#           [1,2,3,3]]  20 21 22 23 XX    321
#                                         4321
#            
# 

def diagonalSort(mat, compare):
    # 1. make diagonal lists
    diagonalList = []
    counter = 0
    blankline = []
    for y in range(len(mat)):
        for x in range(len(mat[y])):                
            for diag in range(len(mat)): 
                if y == 0:
                    try:
                        # diagonalList[counter].append(mat[y+diag][x+diag])
                        diagonalList.append(mat[y+diag][x+diag])
                        if counter == len(mat):
                            counter = 1
                            blankline.append('newline')
                        else:
                            counter = counter + 1
                        blankline.append(counter)
                    except:
                        counter = 0
                        blankline.append('newline')
                        continue
                elif y > 0 and x < 1:
                    try:
                        # diagonalList[counter].append(mat[y+diag][x+diag])
                        diagonalList.append(mat[y+diag][x+diag])
                        if counter == len(mat):
                            counter = 1
                            blankline.append('newline')
                        else:
                            counter = counter + 1
                        blankline.append(counter)
                    except:
                        counter = 0
                        blankline.append('newline')
                        continue
    
    # This gives you how many numbers in diagonal
    counter = 0
    diagonalNumbers = []
    for x in range(len(blankline)):
        if blankline[x] != 'newline':
            counter = counter + 1
        elif counter == 0:
            counter = 0
        else:
            diagonalNumbers.append(counter)
            counter = 0

    #2.  Seperates diagonals / organize diagonal lists
    start = 0
    end = 0
    sortedDiagonalList = []
    for x in range(len(diagonalNumbers)):
        end = end + diagonalNumbers[x]
        sortedL= diagonalList[start:end]
        sortedL.sort()
        sortedDiagonalList.append(sortedL)
        start = start + diagonalNumbers[x]
    print(sortedDiagonalList) 

    # 3. convert back into list 
   
    # Output: [ [1,1,1,1],  00 01 02 03 XX    1
    #           [1,2,2,2],  10 11 12 13 XX    21       
    #           [1,2,3,3]]  20 21 22 23 XX    321
    # [[1, 2, 3],   00 11 22
    #  [1, 2, 3],   01 12 23
    #  [1, 2],      02 13
    #  [1],         03
    #  [1, 2],      10 21 
    #  [1]]         22
    #  1 1 1 1
    #  2 2 2 1
    # squre is 4X3
    print(mat)
    newlist = []
    pullist = []
    counter = 0
    y = 0
    for _ in range(int(len(mat) + len(mat[0]) - 1)):
        newlist.append([])
    
    for x in range(len(sortedDiagonalList[y])):
        for y in range(len(sortedDiagonalList)):
            try:
                pullist.append(sortedDiagonalList[y][x])
            except:
                continue
    print(pullist)
    for x in range(len(pullist)):
        if x < len(mat[0]):
            newlist[0].append(pullist[x])
        elif x > len(mat[0]) and x < len(mat[0]) + len(mat) -1:
            for y in range(1,len(mat)):
                newlist[y].append(pullist[x])
        
        else:
            continue
    print(newlist)
    print(len(mat))

    # 4. return value
    
diagonalSort(mat, compare)