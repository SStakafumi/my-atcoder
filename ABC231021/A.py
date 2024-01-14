N = int(input())

TD = [list(map(int, input().split())) for a in range(N)]
for i in range(N):
    TD[i][1] += TD[i][0]
TD.sort()

ans = 0
now = 1

for t, d in TD:
    if now < t:
        now = t
    if t <= now and now <= d:
        ans += 1
        now += 1


print(ans)
