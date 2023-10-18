def LCS(s1, s2):
    L1 = len(s1)
    L2 = len(s2)
    dp = [[0]*(L2+1) for _ in range(L1+1)]

    for i in range(L1-1, -1, -1):
        for j in range(L2-1, -1, -1):
            r = max(dp[i+1][j], dp[i][j+1])
            if s1[i] == s2[j]:
                r = max(r, dp[i+1][j+1] + 1)
            dp[i][j] = r

    # dp[0][0] が最長共通部分列長さの解
    # print(dp[0][0])

    # ここからは復元処理
    res = []
    i = 0
    j = 0
    while i < L1 and j < L2:
        if s1[i] == s2[j]:
            res.append(s1[i])
            i += 1
            j += 1
        elif dp[i][j] == dp[i+1][j]:
            i += 1
        elif dp[i][j] == dp[i][j+1]:
            j += 1
    return "".join(res)


# Input
s1 = input()
s2 = input()

ans = LCS(s1, s2)
print(ans)
