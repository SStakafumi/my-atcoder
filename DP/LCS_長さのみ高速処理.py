def LCS(s1, s2):
    """共通最長文字列長さを求めるだけなら、高速なプログラム"""
    # s1, s2は比較する文字列
    dp = []
    for s2_k in s2:
        bgn_idx = 0
        for i, cur_idx in enumerate(dp):
            chr_idx = s1.find(s2_k, bgn_idx) + 1
            if not chr_idx:
                break
            dp[i] = min(cur_idx, chr_idx)
            bgn_idx = cur_idx
        else:
            chr_idx = s1.find(s2_k, bgn_idx) + 1
            if chr_idx:
                dp.append(chr_idx)
    # dpの長さが最長文字列長さ
    return len(dp)


x = input()
y = input()

print(LCS(x, y))
