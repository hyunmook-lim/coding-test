from collections import deque
dz = [-1, 1]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def change(z, x, y, day):
    global count_plus
    for num in range(2):
        nz = z + dz[num]
        if 0 <= nz < Z:
            if box[nz][x][y] == 0:
                box[nz][x][y] = 1
                q.append([nz, x, y, day + 1])
                count_plus += 1
    for num in range(4):
        nx = x + dx[num]
        ny = y + dy[num]
        if 0 <= nx < X and 0 <= ny < Y:
            if box[z][nx][ny] == 0:
                box[z][nx][ny] = 1
                q.append([z, nx, ny, day + 1])
                count_plus += 1

Y, X, Z = map(int, input().split())

q = deque([])  # [z, x, y]
count_plus = 0
count_zero = 0
count_minus = 0

box = []
for z in range(Z):
    pan = []
    for x in range(X):
        line = list(map(int, input().split()))
        for y in range(len(line)):
            if line[y] == 1:
                q.append([z, x, y, 0])
                count_plus += 1
            elif line[y] == 0:
                count_zero += 1
            else:
                count_minus += 1
        pan.append(line)
    box.append(pan)

if count_zero == 0:
    print(0)
else:
    day = 0
    while q:
        now = q.popleft()
        if now[3] > day:
            day = now[3]
        change(*now)
    if count_plus + count_minus == X*Y*Z:
        print(day)
    else:
        print(-1)