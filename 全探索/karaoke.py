from itertools import combinations

ans = 0
n, m = list(map(int, input().split()))

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

for i, j in combinations(range(m), 2):
    tmp_score = 0
    for k in range(n):
        tmp_score += max(A[k][i], A[k][j])
    ans = max(ans, tmp_score)

print(ans)