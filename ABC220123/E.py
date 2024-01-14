N = int(input())
A = list(map(int, input().split()))

dp_av = [[0]*(N+1) for _ in range(N)]
dp_mid = [[0]*(N+1) for _ in range(N)]

for i in range(N):
    dp_av[i][i+1] = A[i]

for w in range(2, N):  # 幅は2,...,N
    for i in range(N):  # 始点は0,1,...N-1
        j = i+w
        if j > N:
            continue
        dp_av[i][j] = max(dp_av[])
