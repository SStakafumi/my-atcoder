H, W = map(int, input().split())

# iからjに変える時のコストc
C = [list(map(int, input().split())) for _ in range(10)]

# マス目
A = [list(map(int, input().split())) for _ in range(H)]

for k in range(10):
    for s in range(10):
        for t in range(10):
            C[s][t] = min(C[s][t], C[s][k]+C[k][t])

ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == -1 or A[i][j] == 1:
            continue
        ans += C[A[i][j]][1]

print(ans)
