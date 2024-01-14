import sys
from collections import deque

N, M, K = map(int,input().split())
g = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, a = map(int,input().split())
    g[u].append((v, a))
    g[v].append((u, a))

    
swi = set(list(map(int,input().split())))

qq = deque([(0, 1, 1)])
dists = [[-1] * (N + 1) for _ in range(2)]

while qq:
    dist, now, sw_st = qq.popleft()
    if dists[sw_st][now] != -1:
        continue
    dists[sw_st][now] = dist
    # print(qq)
    
    for nex, now_nex_switch in g[now]:
        if sw_st == now_nex_switch:
            qq.append((dist + 1, nex, sw_st))
        else:
            if now in swi:
                if now_nex_switch == 0 and sw_st == 1:
                    qq.append((dist + 1, nex, 0))
                elif now_nex_switch == 1 and sw_st == 0:
                    qq.append((dist + 1, nex, 1))
                    
                    
from pprint import pprint

if dists[0][N] != -1 and dists[1][N] != -1:
    print(min(dists[0][N], dists[1][N]))
elif dists[0][N] != -1:
    print(dists[0][N])
elif dists[1][N] != -1:
    print(dists[1][N])
else:
    print(-1)
    