from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = float('inf')

for c in combinations(range(1, N), K-1):
    cost = 0
    highest = 0
    B = A.copy()
    for i in range(N):
        if i in c:
            if highest >= B[i]:
                cost += max(0, highest-B[i]+1)
                B[i] = highest + 1
        highest = max(highest, B[i])
    ans = min(ans, cost)

print(ans)
