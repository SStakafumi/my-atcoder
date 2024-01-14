import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())
A = []
B = []
C = []

for i in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = [A[0], B[0], C[0]]

for i in range(1, N):
    dp[i][0] = A[i] + max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = B[i] + max(dp[i-1][0], dp[i-1][2])
    dp[i][2] = C[i] + max(dp[i-1][0], dp[i-1][1])

print(max(dp[N-1]))
