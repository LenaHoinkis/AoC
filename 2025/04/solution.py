with open('data.txt', 'r') as file:
    
    #parse
    lines = file.readlines()
    # padded matrix
    size = len(lines)
    matrix = [[0] * (size+2) for _ in range(size+2)]
    for i in range(size):
        for j in range(size):
            if lines[i][j] == '@':
                matrix[i+1][j+1] = 1

    def neighborhood_sum(matrix, r, c):
        total = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                total += matrix[r + dr][c + dc]
        return total

    #part1
    accessable = 0
    for i in range(1 , size+1):
        for j in range(1, size+1):
            if matrix[i][j]==1:
                if neighborhood_sum(matrix,i,j)<5:
                    accessable +=1
    print(accessable)

    #part2
    def remove(matrix):
        accessable = []
        for i in range(1 , size+1):
            for j in range(1, size+1):
                if matrix[i][j]==1:
                    if neighborhood_sum(matrix,i,j)<5:
                        accessable.append((i,j))
        return accessable
        
    result = 0
    while (rolls := remove(matrix)):
        result += len(rolls)
        for i, j in rolls:
            matrix[i][j]=0
    print(result)
