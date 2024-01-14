import itertools as it
n, m = map(int, input().split())

friend = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    friend[x][y] = 1
    friend[y][x] = 1

ans = 0
for bit in range(2**n):
    group = []  # 派閥のリスト
    for i in range(n):
        if (bit >> i) & 1:
            group.append(i+1)  # bitが1ならiさんを派閥にくわえる
    # 派閥の人が互いに知り合いか判定フラグ
    flag = True
    for j in it.combinations(group, 2):
        if friend[j[0]][j[1]] == 0:
            flag = False
            break
    if flag:
        ans = max(ans, len(group))

print(ans)
