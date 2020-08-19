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
    # for _ in range(int(len(mat) + len(mat[0]) - 1)):
    #     diagonalList.append([])
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
                            
    print(diagonalList)
    print(counter)
    
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
    print(diagonalNumbers)
    
    # Seperates diagonals
    for x in range(len(diagonalNumbers)):
        
        print(diagonalNumbers[x])



    # 2. organize diagonal lists

    # 3. convert back into list 
    # 4. return value

diagonalSort(mat, compare)