def box(n):
    square = [i for i in range(n)]
    for column in range(n):
        square[column] = [[] for i in range(n)]

    row = n/2
    column = n/2
    index = 1
    direction = [1,1]
    while 1:
        square[row][column] = index
        row += direction[0]
        column += direction[1]
        #TODO change direction

print box(5)
