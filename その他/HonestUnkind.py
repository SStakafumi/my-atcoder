# g : i番目の人がj番目の人を 正直者(1)、不親切な人(0)、ノーコメント(-1)といったと格納
g = [[-1 for _ in range(15)] for _ in range(15)]
n = int(input())

for i in range(n):
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        g[i][x-1] = y
ans = 0
for i in range(1 << n):
    honests = [0 for _ in range(n)]  # honestsにi番目の人を正直者と仮定(1)した15行リストを格納
    for j in range(n):
        if i >> j & 1:
            honests[j] = 1
    ok = True
    for j in range(n):
        if honests[j]:
            for k in range(n):
                if g[j][k] == -1:
                    continue
                if g[j][k] != honests[k]:
                    ok = False
    if ok:
        ans = max(ans, honests.count(1))

print(ans)
