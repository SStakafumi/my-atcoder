s = int(input())
dp = [0]*s

for i in range(3, s+1):
    cnt = 1
    for j in range(i-3):
        cnt += dp[j]
    dp[i-1] = cnt

print(dp[-1] % (10**9+7))
