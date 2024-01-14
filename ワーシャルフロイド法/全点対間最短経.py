import sys
from math import isinf
def input(): return sys.stdin.readline().rstrip()


V, E = map(int, input().split())

INF = float('INF')

graph = [[INF]*V for _ in range(V)]
for _ in range(E):
    s, t, d = map(int, input().split())
    graph[s][t] = d


for i in range(V):
    graph[i][i] = 0

for k in range(V):
    for s in range(V):
        for t in range(V):
            graph[s][t] = min(graph[s][t], graph[s][k] + graph[k][t])
            if graph[s][s] < 0:
                print("NEGATIVE CYCLE")
                sys.exit()


for g in graph:
    print(" ".join(["INF" if isinf(gi) else str(gi) for gi in g]))
