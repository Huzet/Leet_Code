mat = [ [3,3,1,1],
        [2,2,1,2],
        [1,1,1,2] ]

organized = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]

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