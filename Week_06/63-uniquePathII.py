def findP(input):
    if input[0][0] == 1:
        return 0
    input[0][0] = 1
    rows = len(input)
    cols = len(rows[0])
    for c in range(cols):
        input[0][c] == int(input[0][c] == 0 and input[0][c-1] == 1)
    for r in len(rows):
        input[r][0] == int(input[r][0] == 0 and input[r-1][0] == 1)
    for i in range(1, rows):
        for j in range(1, cols):
            if input[i][j] == 0:
                input[i][j] = input[i-1][j] + input[i][j-1]
            else:
                input[i][j] = 0
    return input[rows-1][cols-1]
