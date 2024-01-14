import bisect


def LIS(seq):
    """LIS関数"""
    dp = [seq[0]]
    for i in range(N):
        if seq[i] > dp[-1]:
            dp.append(seq[i])
        else:
            dp[bisect.bisect_left(dp, seq[i])] = seq[i]
    return dp


# 配列の長さ(6 など)
N = int(input())
# seqは考える数列(1 3 5 2 4 6 など)
seq = list(map(int, input().split()))

# dpの長さが最長増加部分列の長さ
print(len(LIS(seq)))

# dpの要素が最長増加部分列の数列のひとつ
# print(dp)
print("".join(map(str, LIS(seq))))
