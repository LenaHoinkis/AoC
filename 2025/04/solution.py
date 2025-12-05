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

    def find_accessable(matrix):
        accessable = []
        for i in range(1 , size+1):
            for j in range(1, size+1):
                if matrix[i][j]==1:
                    if neighborhood_sum(matrix,i,j)<5:
                        accessable.append((i,j))
        return accessable

    #part1
    print(len(find_accessable(matrix)))

    #part2
    result = 0
    while (accessable := find_accessable(matrix)):
        result += len(accessable)
        for i, j in accessable:
            matrix[i][j]=0
    print(result)
