# 合わない ...問題の意味がわからないのでパス
# 考え方はあってそう

import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
RC = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(0)
    sys.exit()

INF = float('INF')

# dp[i][j] = 半開区間[i,j]で連鎖行列積をする時の最初計算回数。ただし幅をwと考えj = i+wとする
dp = [[INF]*(N+1) for _ in range(N)]

for k in range(N):
    dp[k][k+1] = 0

for w in range(2, N+1):
    for i in range(N):
        j = i+w
        if j > N:
            continue
        dp[i][j] = min(dp[i][j-1] + RC[i][0]*RC[j-2][1]*RC[j-1][1],
                       dp[i+1][j] + RC[i][0]*RC[i][1]*RC[j-1][1])

for d in dp:
    print(d)
