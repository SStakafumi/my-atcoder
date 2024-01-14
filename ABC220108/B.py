from itertools import combinations

n = int(input())
XY = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for p1, p2 in combinations(XY, 2):
    dis = ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    ans = max(ans, dis)

print(ans)
