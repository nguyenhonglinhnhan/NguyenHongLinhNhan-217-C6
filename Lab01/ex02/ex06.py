input_str = input("Nhập X,y:")
deimensions = [int(x) for x in input_str.split(',')]
rowNum = deimensions[0]
colNum = deimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col] = row * col
print(multilist)