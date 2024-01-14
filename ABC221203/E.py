import sys
import math

R = 998244353

N, P = map(int, input().split())

dp = [(0, 0) for i in range(max(2, N))]
dp[0] = (1, 1)
dp[1] = (200-P, 100)

# for ループ
for i in range(2, N):
    x1, y1 = dp[i-1]
    x2, y2 = dp[i-2]
    kodomo, haha = y2*(x1+y1)*(100-P)+y1*P*(x2+y2), 100*y1*y2
    dp[i] = kodomo%R, haha%R

p, q = dp[N-1]
r = pow(q, 998244353-2, 998244353)
print((p*r)% R)