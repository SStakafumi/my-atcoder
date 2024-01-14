from collections import defaultdict
Q = int(input())
S = defaultdict(int)

for _ in range(Q):
    qur = list(map(int, input().split()))
    if qur[0] == 1:
        S[qur[1]] += 1
    elif qur[0] == 2:
        x, c = qur[1:]
        cx = S[x]
        S[x] -= min(c, cx)
        if S[x] == 0:
            del S[x]
    else:
        print(max(S)-min(S))
