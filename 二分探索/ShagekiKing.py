def is_ok(mid):
    ls = []
    for i in range(N):
        ls.append((mid-H[i])//S[i])  # いつまでに割れば良いか
    ls.sort()  # 期限が近いものから先にわる
    print(ls)
    for n in range(N):
        if (ls[n] < n):
            return False  # 時間ぎれ
    return True


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
        print(ng)
        print(ok)
    return ok


N = int(input())
H = []
S = []
for i in range(N):
    h, s = map(int, input().split())
    H.append(h)
    S.append(s)
print(meguru_bisect(0, int(1e+14)))
