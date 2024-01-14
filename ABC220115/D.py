from collections import deque

a, N = map(int, input().split())

M = 1
while M <= N:
    # グラフの頂点の値の最大値はNの桁Aよりも大きいA+1桁の値である
    M *= 10

dist = [-1]*M
q = deque()
q.append(1)
dist[1] = 0

while len(q):
    c = q.popleft()
    dc = dist[c]

    op1 = a*c
    if op1 < M and dist[op1] == -1:
        dist[op1] = dc+1
        q.append(op1)

    if c >= 10 and c % 10 != 0:
        s = str(c)
        op2 = int(s[-1]+s[:-1])
        if op2 < M and dist[op2] == -1:
            dist[op2] = dc + 1
            q.append(op2)

print(dist[N])
