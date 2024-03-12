def knapsack_dp(W, wt, val, N):
    A = [[0]*(W+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for w in range(1, W+1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valwith = val[i-1] + A[i-1][w-wt[i-1]]
                valwithout = A[i-1][w]
                A[i][w] = max(valwith, valwithout)
    return A[N][W]

N, W = map(int, input().split())

wt = []
val = []
for _ in range(N):
    w, v = map(int, input().split())
    wt.append(w)
    val.append(v)

print(knapsack_dp(W, wt, val, N))