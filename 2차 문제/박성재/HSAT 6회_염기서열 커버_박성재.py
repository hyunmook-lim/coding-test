import copy
def same(list1, list2):
    for i in range(M):
        if list1[i] & list2[i] == set():
            return False
    else:
        return True

def change(list1, list2):
    for i in range(M):
        set1 = list1[i] & list2[i]
        if set1 != {'a', 'g', 'c', 't'}:
            if list1[i] == {'a', 'g', 'c', 't'}:
                list1[i] = set1
            if list2[i] == {'a', 'g', 'c', 't'}:
                list2[i] = set1

N, M = map(int, input().split())
old = []
for _ in range(N):
    DNA = list(input())
    count = 0
    for i in range(M):
        if DNA[i] != '.':
            DNA[i] = set(DNA[i])
            count += 1
        else:
            DNA[i] = {'a', 'g', 'c', 't'}
    DNA += [count]
    old.append(DNA)

new = []
for i in range(N):
    count = 0
    for j in range(i):
        if not same(old[i], old[j]):
            count += 1
    for j in range(i+1, N):
        if not same(old[i], old[j]):
            count += 1
    new.append([old[i], count])
new = sorted(new, key=lambda x:(x[1], x[0][M]))

max_num = N
for i in range(N):
    copy_list = copy.deepcopy(new)
    q = []
    first = copy_list.pop(i)
    q.append(first)
    while copy_list:
        count = 0
        now = copy_list.pop()
        for q_list in q:
            if same(now[0], q_list[0]):
                count += 1
                change(now[0], q_list[0])
        if count == 0:
            q.append(now)
    if len(q) < max_num:
        max_num = len(q)

print(max_num)