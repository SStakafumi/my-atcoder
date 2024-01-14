import math

INF = float('INF')
N, K = map(int, input().split())
A = list(map(int, input().split()))
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

min_distances = []

for i in range(N):
    if i+1 in A:
        continue
    dis = INF
    for j in A:
        tmp_dis = (X[i]-X[j-1])**2 + (Y[i]-Y[j-1])**2
        dis = min(dis, tmp_dis)
    min_distances.append(dis)

ans = math.sqrt(max(min_distances))
print(ans)
