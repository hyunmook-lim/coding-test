from collections import deque

def move(data, turn):
    for i in range(4):
        if turn[i] == -1:    # 반시계
            change = data[i].popleft()
            data[i].append(change)
        elif turn[i] == 1:    # 시계
            change = data[i].pop()
            data[i].appendleft(change)

def turn_baki(data, number, turn_direction):
    turn = [0]*4
    real = number-1    # 여기서는 1번이 0번 톱니이다.
    turn[real] = turn_direction
    if real == 0:    # 시작 톱니가 0인 경우
        if data[0][2] != data[1][6]:
            turn[1] = -turn[0]
            if data[1][2] != data[2][6]:
                turn[2] = -turn[1]
                if data[2][2] != data[3][6]:
                    turn[3] = -turn[2]
    elif real == 1:    # 시작 톱니가 1인 경우
        if data[0][2] != data[1][6]:
            turn[0] = -turn[1]
        if data[2][6] != data[1][2]:
            turn[2] = -turn[1]
            if data[2][2] != data[3][6]:
                turn[3] = -turn[2]
    elif real == 2:    # 시작 톱니가 2인 경우
        if data[3][6] != data[2][2]:
            turn[3] = -turn[2]
        if data[1][2] != data[2][6]:
            turn[1] = -turn[2]
            if data[0][2] != data[1][6]:
                turn[0] = -turn[1]
    else:    # 시작 톱니가 3인 경우
        if data[2][2] != data[3][6]:
            turn[2] = -turn[3]
            if data[1][2] != data[2][6]:
                turn[1] = -turn[2]
                if data[0][2] != data[1][6]:
                    turn[0] = -turn[1]
    move(data, turn)

data = [deque(map(int, input())) for _ in range(4)]
N = int(input())
for _ in range(N):
    number, turn_direction = map(int, input().split())
    turn_baki(data, number, turn_direction)

sum_num = 0
for i in range(4):
    if i == 0:
        if data[i][0] == 1:
            sum_num += 1
    elif i == 1:
        if data[i][0] == 1:
            sum_num += 2
    elif i == 2:
        if data[i][0] == 1:
            sum_num += 4
    else:
        if data[i][0] == 1:
            sum_num += 8
print(sum_num)