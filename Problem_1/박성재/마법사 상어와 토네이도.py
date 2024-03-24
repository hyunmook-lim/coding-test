# 토네아도 움직임: 좌 하 우 상 반복!
import pprint

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
check_x = [[0, -1, 1, 1, -1, 2, -2, -1, 1],
           [2, 1, 1, 0, 0, 0, 0, -1, -1],
           [0, 1, -1, -1, 1, -2, 2, 1, -1],
           [-2, -1, -1, 0, 0, 0, 0, 1, 1]]
check_y = [[-2, -1, -1, 0, 0, 0, 0, 1, 1],
           [0, 1, -1, -1, 1, -2, 2, -1, 1],
           [2, 1, 1, 0, 0, 0, 0, -1, -1],
           [0, -1, 1, 1, -1, 2, -2, 1, -1]]
multi = [5, 10, 10, 7, 7, 2, 2, 1, 1]
def tornado(now, count, stop, direction, baram):
    global out
    global start
    if now != [N//2, N//2]:
        all = graph[now[0]][now[1]]
        for i in range(9):
            nx = now[0] + check_x[baram][i]
            ny = now[1] + check_y[baram][i]
            if 0 <= nx < N and 0 <= ny < N:
                graph[nx][ny] += multi[i] * graph[now[0]][now[1]]//100
                all -= multi[i] * graph[now[0]][now[1]]//100
            else:
                out += multi[i] * graph[now[0]][now[1]]//100
                all -= multi[i] * graph[now[0]][now[1]]//100
        nx = now[0] + dx[baram]
        ny = now[1] + dy[baram]
        if 0 <= nx < N and 0 <= ny < N:
            graph[nx][ny] += all
        else:
            out += all

    nx = now[0] + dx[direction]
    ny = now[1] + dy[direction]
    if 0 <= nx < N and 0 <= ny < N:
        if count != stop:
            q.append([[nx, ny], count + 1, start // 2, direction, direction])
        else:
            start += 1
            q.append([[nx, ny], 0, start // 2, (direction + 1) % 4, direction])
    graph[now[0]][now[1]] = 0

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
q = []
out = 0
start = 0
q.append([[N//2, N//2], 0, 0, 0, 0])
while q:
    now = q.pop()
    tornado(*now)

print(out)