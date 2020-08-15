#! Python3

# https://leetcode.com/problems/sort-the-matrix-diagonally/

# Input: 
mat = [ [3,3,1,1],
        [2,2,1,2],
        [1,1,1,2]]

compare = [3,2,1,3,1,2,1,2,1,2,1,1]
# Output: [ [1,1,1,1],  00 01 02 03 XX    1
#           [1,2,2,2],  10 11 12 13 XX    21       
#           [1,2,3,3]]  20 21 22 23 XX    321
#                                         4321
#            
# 

def diagonalSort(mat, compare):
    # 1. make diagonal lists
    diagonalList = []
    for _ in range(int(len(mat) + len(mat[0]) - 1)):
        diagonalList.append([])
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            for diag in range(len(mat)):
                if y == 0:
                    try:
                        diagonalList[x].append(mat[y+diag][x+diag])
                    except:
                        continue
                elif y > 0 and x < 1:
                    try:
                        diagonalList[x].append(mat[y+diag][x+diag])
                    except:
                        continue
    if diagonalList == compare:
        print('we got a match')
    else:
        print('does not match')
    print("length of list is", + len(diagonalList))
    print(diagonalList)

    # 2. organize diagonal lists
            
    # 3. convert back into list
    # 4. return value

diagonalSort(mat, compare)