#! Python3

# https://leetcode.com/problems/sort-the-matrix-diagonally/

# Input: 
mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]

def diagonalSort(mat):
    # 1. make diagonal lists
    diagonalList = []
    counter = 0
    blankline = []
    for y in range(len(mat)):
        for x in range(len(mat[y])):                
            for diag in range(len(mat)): 
                if y == 0:
                    try:
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
    # print(sortedDiagonalList) 

    # 3. convert back into list 
    organized = []
    counter = 0
    y = 0

    for x in range(len(sortedDiagonalList[y])):
        for y in range(len(sortedDiagonalList)):
            try:
                organized.append(sortedDiagonalList[y][x])
            except:
                continue
    # print(organized)

    # 4. return value
    newlist = []

    for _ in range(len(mat)):
        newlist.append([])

    lengthL = len(mat[0]) # 4
    heightL = ( len(mat)-1 + len(mat[0]) ) # 6

    line = 0
    placeholderLine = 0

    for x in range(len(organized)):
        if x < lengthL:
            newlist[line].append(organized[x])
        elif x >= lengthL and x < heightL:
            placeholderLine = placeholderLine + 1
            newlist[placeholderLine].append(organized[x])
        else: 
            line = line + 1
            placeholderLine = line
            lengthL = heightL + ( lengthL-1 )
            heightL = lengthL + 1
            if x < lengthL:
                newlist[line].append(organized[x])
    print(newlist)

    
diagonalSort(mat)