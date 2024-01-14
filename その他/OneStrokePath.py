from itertools import permutations

### 解法1 ###
N, M = map(int, input().split())

numSet = [set(map(int, input().split())) for _ in range(M)]
l = list(range(1, N+1))

ans = 0
for per in permutations(l, N):
    if per[0] != 1:
        break
    for i in range(N-1):
        if set([per[i], per[i+1]]) not in numSet:
            break
    else:
        ans += 1

print(ans)

### 解法2 ###
""" 
import itertools

n, m = map(int,input().split())

graph = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1

ans = 0
for num in itertools.permutations(range(n)):
    if num[0] == 0:
        count = 0
        for i in range(n-1):
            if graph[num[i]][num[i+1]] == 1:
                count += 1
        if count == n-1:
            ans += 1

print(ans)
 """
