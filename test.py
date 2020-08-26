mat = [ [3,3,1,1],
        [2,2,1,2],
        [1,1,1,2] ]

newlist = []

organized = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
# for _ in range(int(len(mat) + len(mat[0]) - 1)):
#     newlist.append([])

# counter = len(mat) + len(mat[0]) - 1 # 6
# previousCounter = 0  
# height = len(mat) - 1  # 2
# rotation = 0
# holderrotation = 0
# for x in range(len(organized)):
#     if x < counter + previousCounter - height:
#         newlist[holderrotation].append(organized[x])
#         print('1', x)

#     elif x < counter:        
#         holderrotation = holderrotation + 1
#         newlist[holderrotation].append(organized[x])
#         print('2', x)

#     else:
#         rotation = rotation + 1
#         holderrotation = rotation
#         counter = ( len(mat) + len(mat[0]) - (rotation * 2) ) + counter
#         print(counter)
#         height = height - 1
#         if x < counter + previousCounter - height:
#             newlist[holderrotation].append(organized[x])
#             print('3', x)

#         elif x < counter:        
#             holderrotation = holderrotation + 1
#             newlist[holderrotation].append(organized[x])
#             print('4', x)
         

print(len(mat) - 1)


