rectangle_row_dx = [[0, 1, 1, 1],
                    [0, 1, 1, 1],
                    [0, 0, 0, 1],
                    [0, 0, 0, 1],
                    [0, 1, 1, 1],
                    [0, 0, 0, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1],
                    [0, 0, 1, 1]]
rectangle_row_dy = [[2, 0, 1, 2],
                    [0, 0, 1, 2],
                    [0, 1, 2, 2],
                    [0, 1, 2, 0],
                    [1, 0, 1, 2],
                    [0, 1, 2, 1],
                    [1, 2, 0, 1],
                    [0, 1, 1, 2],
                    [1, 2, 1, 2],
                    [0, 1, 0, 1]]
rectangle_column_dx = [[0, 1, 2, 2],
                       [0, 1, 1, 2],
                       [0, 1, 2, 2],
                       [0, 1, 1, 2],
                       [0, 0, 1, 2],
                       [0, 1, 1, 2],
                       [0, 0, 1, 2],
                       [0, 1, 1, 2],
                       [1, 1, 2, 2],
                       [0, 0, 1, 1]]
rectangle_column_dy = [[1, 1, 0, 1],
                       [1, 0, 1, 1],
                       [0, 0, 0, 1],
                       [1, 0, 1, 0],
                       [0, 1, 1, 1],
                       [0, 0, 1, 1],
                       [0, 1, 0, 0],
                       [0, 0, 1, 0],
                       [0, 1, 0, 1],
                       [0, 1, 0, 1]]
stick_row_dx = [0, 0, 0, 0]
stick_row_dy = [0, 1, 2, 3]
stick_column_dx = [0, 1, 2, 3]
stick_column_dy = [0, 0, 0, 0]

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
max_num = 0

# rectangle_row 탐색
for i in range(N-1):
    for j in range(M-2):
        for n in range(10):
            sum_num = 0
            for m in range(4):
                sum_num += graph[i+rectangle_row_dx[n][m]][j+rectangle_row_dy[n][m]]
            if sum_num > max_num:
                max_num = sum_num
# rectangle_column 탐색
for i in range(N-2):
    for j in range(M-1):
        for n in range(10):
            sum_num = 0
            for m in range(4):
                sum_num += graph[i+rectangle_column_dx[n][m]][j+rectangle_column_dy[n][m]]
            if sum_num > max_num:
                max_num = sum_num
# stick_row 탐색
for i in range(N):
    for j in range(M-3):
        sum_num = 0
        for m in range(4):
            sum_num += graph[i + stick_row_dx[m]][j + stick_row_dy[m]]
        if sum_num > max_num:
            max_num = sum_num
# stick_column 탐색
for i in range(N-3):
    for j in range(M):
        sum_num = 0
        for m in range(4):
            sum_num += graph[i + stick_column_dx[m]][j + stick_column_dy[m]]
        if sum_num > max_num:
            max_num = sum_num
print(max_num)