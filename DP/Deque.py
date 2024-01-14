import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())
A = [0] + list(map(int, input().split()))

# dp[i][j] = 数列の要素がindex,iからj+1まで残っているとき次の人の総得点-次の次の人の総得点の最大値
dp = [[0]*(N+2) for _ in range(N+1)]

for w in range(1, N+2):
    for i in range(1, N+1):
        j = i+w
        if j > N+1:
            continue
        if w == 1:
            # もし幅が1だったら
            dp[i][j] = A[i]
        else:
            dp[i][j] = max(A[i]-dp[i+1][j], A[j-1]-dp[i][j-1])

print(dp[1][N+1])
