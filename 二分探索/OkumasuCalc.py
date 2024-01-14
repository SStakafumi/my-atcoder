from bisect import bisect
import sys
read = sys.stdin.readline


def read_ints():
    return list(map(int, read().split()))


N, K = read_ints()
A = read_ints()
B = read_ints()
A.sort()
B.sort()


def is_ok(X):
    # a_i * b_j <= Xを満たす個数がK個以上か
    cnt = 0
    for a in A:
        aa = X // a
        cnt += bisect(B, aa)  # 配列の二分探索はめぐる式でなくて良い
    return cnt >= K


def meguru_bisect(ng, ok):
    # is_okを満たす最小のXを返す
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, 10 ** 18 + 1))
