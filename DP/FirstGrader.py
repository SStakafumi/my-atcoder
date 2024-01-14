import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
A = list(map(int, input().split()))
M = 20
dp = [[0]*(M+1) for _ in range(N-1)]
dp[0][A[0]] = 1

for i in range(1, N-1):
    for j in range(M+1):
        if j-A[i] >= 0:
            dp[i][j] += dp[i-1][j-A[i]]
        if j+A[i] <= M:
            dp[i][j] += dp[i-1][j+A[i]]
print(dp[-1][A[-1]])
